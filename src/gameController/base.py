import sys
import argparse
from wordController.base import WordController
from painter.base import BasePainter
from recorder.base import BaseRecorder

class GameController:
    
    def __init__(self, args):
        parser = argparse.ArgumentParser(description = '<<< The Game Hangman >>>')
        parser.add_argument('--no-report',
            help = 'turn off the report after the end of the game',
            action = 'store_true')
        args = parser.parse_args(args)
        self.report = not args.no_report

    def new_game(self):
        self.wordController = WordController()
        self.recorder = BaseRecorder(self.wordController)

        self.wordController.display_word()

        while self.recorder.has_guessed_word() is not True:
            self.recorder.request_letter()

        print("Well done!")