from .base import BaseWordGenerator
from utility.word import Word
from random import randint

class Fruit(BaseWordGenerator):

	def get_word(self):
		words = self.generate_words()
		selected_word = words[randint(0, len(words)-1)]
		return Word(words[randint(0, len(words)-1)])

	def generate_words(self):
		words = [
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

		return words