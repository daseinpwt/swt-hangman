from .base import BaseWordGenerator
from random import randint

class Fruit(BaseWordGenerator):

    def get_word(self):
        words = self.generate_words()
        return list(words[randint(0, len(words)-1)])

    def generate_words(self):
        return [
            "apple",
            "lemon",
            "banana",
            "strawberry",
            "pineapple",
            "peach",
            "kiwi",
            "grape",
            "orange",
            "cherry",
            "melon",
            "grapefruit",
        ]
