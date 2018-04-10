from random import randint
from recorder.base import BaseRecorder

class WordController:

	def __init__(self):
		self.word = list(self.generate_word())

	def new_word(self):
		self.word = list(self.generate_word())

	def generate_word(self):
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

		return words[randint(0, len(words)-1)]

	def display_word(self, selected_letters = []):
		display_string = ""
		for letter in self.word:
			has_guessed = False

			for guessed_letter in selected_letters:
				if letter == guessed_letter:
					has_guessed = True

			if has_guessed:
				display_string += " {} ".format(letter)
			else:
				display_string += " - "

		print("{}".format(display_string))

	def is_letter_in_word(self, letter):
		letter_in_word = False
		for l in self.word:
			if l == letter:
				letter_in_word = True

		return letter_in_word