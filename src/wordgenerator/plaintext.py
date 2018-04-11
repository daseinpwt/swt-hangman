import os
from .base import BaseWordGenerator
from random import randint

class Plaintext(BaseWordGenerator):

    def get_word(self, filename):
        words = self.generate_words(filename)
        return list(words[randint(0, len(words)-1)])

    def generate_words(self, filename):
        file = open(self.format_filename(filename), "r")
        words = file.read().splitlines()
        return words

    def format_filename(self, filename):
        extention = ".txt"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return "{}/text/{}{}".format(dir_path, filename, extention)