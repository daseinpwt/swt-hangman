from .base import BaseWordGenerator
from random import randint

class Fruit(BaseWordGenerator):

    def __init__(self):
        self.words = [
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

    def getWord(self):
        return list(self.words[randint(0, len(self.words)-1)])
