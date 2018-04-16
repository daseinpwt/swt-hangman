from .gameplayController import GameplayController
import wordgenerator

class SingleplayerController(GameplayController):
    def new_game(self):
        self.selected_letters = []
        self.number_of_fails = 0

        self.word_generator = wordgenerator.get('fruit')
        self.word = self.word_generator.get_word()
        self.word.display_masked_word(self.selected_letters)

        while not self.has_guessed_word():
            letter_input = input('Insert letter: ') # Request user input
            letter_input = self.format_input(letter_input) # Format input, trim and convert to lowercase

            # Check if the letter has already been entered by the user
            if self.has_used_letter(letter_input):
                print("The letter has already been used! {}".format(self.selected_letters))
                print("You made {} mistakes".format(self.number_of_fails))
            else:
                # Update number of tries when input letter is NOT in the word
                if not self.word.is_letter_in_word(letter_input):
                    self.number_of_fails += 1

                # Add the new letter to the list of used letters
                self.selected_letters.append(letter_input)
                print("Selected letters: {}".format(self.selected_letters))
                print("You made {} mistakes".format(self.number_of_fails))
                self.word.display_masked_word(self.selected_letters)

        print("Well done! You have {} number of fails...".format(self.number_of_fails))

    # Format input letter (lower case and strip spaces)
    def format_input(self, letter):
        string_to_format = letter
        string_to_format = string_to_format.lower()
        string_to_format = string_to_format.strip()
        return string_to_format

    # Method which returns true if the complete word has been guessed
    def has_guessed_word(self):
        count = 0
        for letter in self.word.characters:
            for guessed_letter in self.selected_letters:
                if letter == guessed_letter:
                    count += 1
                    break

        if count == len(self.word.characters):
            return True

        return False

    # Method which returns true if the letter has already been used 
    def has_used_letter(self, letter_input):
        has_already_used_letter = False
        for letter in self.selected_letters:
            if letter == letter_input:
                has_already_used_letter = True
        return has_already_used_letter