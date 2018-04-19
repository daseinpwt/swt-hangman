import argparse
from painter.base import BasePainter
from recorder.base import BaseRecorder
from .gameplayController import GameplayController
import sys
import wordgenerator

MAX_FAILS = 8

class ReplayController(GameplayController):
    def __init__(self, args = []):
        parser = argparse.ArgumentParser(description = '<<< The Game Hangman >>>')
        parser.add_argument('--no-report',
            help = 'turn off the report after the end of the game',
            action = 'store_true')
        args = parser.parse_args(args)
        self.report = not args.no_report

    def new_game(self):
        print('========================')
        print('Welcome to Hangman Game!')
        print('========================')
        self.game_idx = 0

        while True:
            # game start
            self.game_idx = self.game_idx + 1
            print(" <<<      Game %s     >>>\n" % self.game_idx)

            self.word_generator = wordgenerator.get('fruit')
            self.word = self.word_generator.get_word().to_string()
            self.guess = [False] * len(self.word)
            self.painter = BasePainter(MAX_FAILS)
            self.recorder = BaseRecorder()
            self.num_fails = 0
            self.step = 0

            while self.run():
                pass

            if self.report:
                self.recorder.report()

            while True:
                cont = input("do you want to continue? (y/n): ")
                if cont == 'y':
                    break
                elif cont == 'n':
                    return
                else:
                    print('Please enter y or n!')

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
