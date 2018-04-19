from .base import BaseWordGenerator
from .word import Word
from random import randint

class Fruit(BaseWordGenerator):
    def get_word(self):
        words = self.generate_words()
        selected_word = words[randint(0, len(words)-1)]
        return Word(selected_word)

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
