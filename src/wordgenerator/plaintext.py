import sys
import os
from .base import BaseWordGenerator
from .word import Word
from random import randint

class Plaintext(BaseWordGenerator):

    def get_word(self): # Throw error, plaintext files need to be opened with filename
        raise ValueError('PlaintextWordGenerator get_word(), you should use get_word_with_filename() instead')

    def generate_words(self, filename):
        pass

    def get_word_with_filename(self, filename):
        file_location = self.format_filename(filename)

        # Check if the file exists else throw error
        if os.path.exists(file_location):
            words = self.open_plaintext_file(file_location)
            selected_word = words[randint(0, len(words)-1)]
            return Word(selected_word)
        else:
            raise ValueError("No such file {}".format(file_location))

    # Open the file and read words, every new line is a word
    def open_plaintext_file(self, location):
        with open(location, 'r') as file:
            return file.read().splitlines()

    # Formats filepath, current filepath is set to /text folder inside wordgenerator
    def format_filename(self, filename):
        extention = ".txt"
        if hasattr(sys, '_MEIPASS'):
            dir_path = sys._MEIPASS + '/wordgenerator'
        else:
            dir_path = os.path.dirname(os.path.realpath(__file__))
        return "{}/text/{}{}".format(dir_path, filename, extention)
