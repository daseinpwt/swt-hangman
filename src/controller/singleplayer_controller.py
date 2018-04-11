from .gameplay_controller import Gameplay_Controller
import wordgenerator

class Singleplayer_Controller(Gameplay_Controller):

	def new_game(self):
		self.selected_letters = []
		self.number_of_fails = 0

		self.word_generator = wordgenerator.get('fruit')
		self.word = self.word_generator.get_word()
		self.word.display_masked_word(self.selected_letters)

	def run_game(self):
		while not self.has_guessed_word():
			letter_input = input('Insert letter: ') # Request user input
			letter_input = self.format_input(letter_input) # Format input, trim and convert to lowercase

			# Check if the letter has already been entered by the user
			has_already_used_letter = False
			for letter in self.selected_letters:
				if letter == letter_input:
					has_already_used_letter = True

			if has_already_used_letter:
				print("The letter has already been used! {}".format(self.selected_letters))
				print("You made {} mistakes".format(self.number_of_fails))
			else:
				# Update number of tries when input letter is NOT in the word
				if not self.word.is_letter_in_word(letter_input):
					self.number_of_fails += 1

				self.selected_letters.append(letter_input)
				print("Selected letters: {}".format(self.selected_letters))
				print("You made {} mistakes".format(self.number_of_fails))
				self.word.display_masked_word(self.selected_letters)

		print("Well done! You have {} number of fails...".format(self.number_of_fails))

	def format_input(self, letter):
		string_to_format = letter
		string_to_format = string_to_format.lower()
		string_to_format = string_to_format.strip()
		return string_to_format

	def has_guessed_word(self):
		count = 0
		for letter in self.word.characters:
			has_guessed = False

			for guessed_letter in self.selected_letters:
				if letter == guessed_letter:
					has_guessed = True

			if has_guessed:
				count += 1

		guessed_word = False
		if count == len(self.word.characters):
			guessed_word = True

		return guessed_word