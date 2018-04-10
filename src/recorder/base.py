import os

class BaseRecorder:

    def __init__(self, wordController):
        self.selected_letters = []
        self.number_of_fails = 0
        self.wordController = wordController

    def request_letter(self):
        letter_input = input('Insert letter: ') # Request user input
        letter_input = self.format_input(letter_input) # Format input, trim and convert to lowercase

        # Check if the letter has already been entered by the user
        letter_in_list = False
        for letter in self.selected_letters:
            if letter == letter_input:
                letter_in_list = True

        # If inserted letter has not been entered before, add letter to selected_letters and update display 
        if letter_in_list is not True:
            os.system('clear') # Unix console clearing
            os.system('cls') # Windows console clearing 

            # Update number of tries when input letter is NOT in the word
            if not self.wordController.is_letter_in_word(letter_input):
                self.number_of_fails += 1

            self.selected_letters.append(letter_input)
            print("Selected letters: {}".format(self.selected_letters))
            print("You made {} mistakes".format(self.number_of_fails))
            self.wordController.display_word(self.selected_letters)

        # If the letter has already been used by the user
        else:
            print("The letter has already been used! \n {}".format(self.selected_letters))
            print("You made {} mistakes".format(self.number_of_fails))

    def format_input(self, letter): # Format input, trim and convert to lowercase
        string_to_format = letter
        string_to_format = string_to_format.lower()
        string_to_format = string_to_format.strip()
        return string_to_format

    def has_guessed_word(self): # Checks if user has fully unlocked the word
        count = 0
        for letter in self.wordController.word:
            has_guessed = False

            for guessed_letter in self.selected_letters:
                if letter == guessed_letter:
                    has_guessed = True

            if has_guessed:
                count += 1

        guessed_word = False
        if count == len(self.wordController.word):
            guessed_word = True

        return guessed_word
