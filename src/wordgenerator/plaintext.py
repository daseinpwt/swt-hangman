import sys, os
from .base import BaseWordGenerator
from .word import Word
from random import randint

class Plaintext(BaseWordGenerator):

    def get_word(self): 
        raise ValueError('PlaintextWordGenerator get_word(), you should use get_words_with_filename() instead')

    def generate_words(self, filename):
        pass

    def get_words_with_filename(self, filename):
        file_location = self.format_filename(filename)
        if os.path.exists(file_location):
            words = self.open_plaintext_file(file_location)
            selected_word = words[randint(0, len(words)-1)]
            return Word(selected_word)
        else:
            raise ValueError("No such file {}".format(file_location))

    def open_plaintext_file(self, location):
        with open(location, 'r') as file:
            return file.read().splitlines()

    def format_filename(self, filename):
        extention = ".txt"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return "{}/text/{}{}".format(dir_path, filename, extention)