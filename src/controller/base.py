import argparse
from wortschatz.base import BaseWortschatz
from painter.base import BasePainter
from recorder.base import BaseRecorder
import sys

MAX_FAILS = 3

class BaseController:
    def __init__(self, args):
        parser = argparse.ArgumentParser(description='<<< The Game Hangman >>>')
        parser.add_argument("--no-report",
            help="turn off the report after the end of the game",
            action="store_true")
        args = parser.parse_args(args)
        self.no_report = args.no_report

    def start(self):
        # game start
        self.wortschatz = BaseWortschatz()
        self.word = self.wortschatz.newWord()
        self.guess = [False] * len(self.word)
        self.painter = BasePainter(MAX_FAILS)
        self.recorder = BaseRecorder()
        self.count = 0
        self.numFails = 0
        self.step = 0

        while self.run():
            pass

        if not self.no_report:
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
