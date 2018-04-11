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
        self.word_generator = wordgenerator.get('fruit')
        self.word = ''.join(self.word_generator.get_word())
        self.guess = [False] * len(self.word)
        self.painter = BasePainter(MAX_FAILS)
        self.recorder = BaseRecorder()
        self.num_fails = 0
        self.step = 0

        while self.run():
            pass

        if self.report:
            self.recorder.report()

    def run(self):
        self.step = self.step + 1
        guess_char = self.painter.get_new_guess()
        # print("you have guessed %c" % guessChar)
        success = False
        for i, c in enumerate(self.word):
            if c == guess_char:
                self.guess[i] = True
                success = True
        if not success:
            self.num_fails = self.num_fails + 1

        self.recorder.record(self.step, list(self.guess), self.word, self.num_fails)

        if (self.num_fails == MAX_FAILS):
            self.painter.draw_lose_state(self.guess, self.word)
            return False
        if all(self.guess):
            self.painter.draw_win_state(self.word, self.num_fails)
            return False
        else:
            self.painter.draw_current_state(self.guess, self.word, self.num_fails)
            return True
