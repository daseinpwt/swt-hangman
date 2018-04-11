import argparse
from painter.base import BasePainter
from recorder.base import BaseRecorder
import sys
import wordgenerator

MAX_FAILS = 3

class BaseController:
    def __init__(self, args):
        parser = argparse.ArgumentParser(description = '<<< The Game Hangman >>>')
        parser.add_argument('--no-report',
            help = 'turn off the report after the end of the game',
            action = 'store_true')
        args = parser.parse_args(args)
        self.report = not args.no_report

    def start(self):
        # game start
        self.word_generator = wordgenerator.get('plaintext')
        self.word = ''.join(self.word_generator.get_word("carbrands"))
        self.guess = [False] * len(self.word)
        self.painter = BasePainter(MAX_FAILS)
        self.recorder = BaseRecorder()
        self.numFails = 0
        self.step = 0

        while self.run():
            pass

        if self.report:
            self.recorder.report()

    def run(self):
        self.step = self.step + 1
        guessChar = self.painter.getNewGuess()
        # print("you have guessed %c" % guessChar)
        success = False
        for i, c in enumerate(self.word):
            if c == guessChar:
                self.guess[i] = True
                success = True
        if not success:
            self.numFails = self.numFails + 1

        self.recorder.record(self.step, list(self.guess), self.word, self.numFails)

        if (self.numFails == MAX_FAILS):
            self.painter.drawLoseState(self.guess, self.word)
            return False
        if all(self.guess):
            self.painter.drawWinState(self.word, self.numFails)
            return False
        else:
            self.painter.drawCurrentState(self.guess, self.word, self.numFails)
            return True
