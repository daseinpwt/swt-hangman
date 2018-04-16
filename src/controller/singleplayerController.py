from .gameplayController import GameplayController
import wordgenerator

class SingleplayerController(GameplayController):
    def new_game(self):
        self.selected_letters = []
        self.number_of_fails = 0

        # TODO: change to painter later
        self.word_generator = wordgenerator.get('plaintext')
        self.word = self.word_generator.get_words_with_filename('default')
        self.word.display_masked_word(self.selected_letters)

        while not self.has_guessed_word():
            letter_input = input('Insert letter: ') # Request user input
            letter_input = letter_input.lower().strip() # Format input, trim and convert to lowercase

            # Check if the letter has already been entered by the user
            if self.has_used_letter(letter_input):
                print("The letter has already been used! {}".format(self.selected_letters))
                print("You made {} mistakes".format(self.number_of_fails))
            else:
                self.update_number_of_fails(letter_input)

                # Add the new letter to the list of used letters
                self.selected_letters.append(letter_input)
                print("Selected letters: {}".format(self.selected_letters))
                print("You made {} mistakes".format(self.number_of_fails))

                # Should be replaced by recorder method
                self.word.display_masked_word(self.selected_letters)

        print("Well done! You have {} number of fails...".format(self.number_of_fails))

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
        for letter in self.selected_letters:
            if letter == letter_input:
                return True
        return False

    # Update number of tries when input letter is NOT in the word
    def update_number_of_fails(self, letter_input):
        if not self.word.is_letter_in_word(letter_input):
            self.number_of_fails += 1