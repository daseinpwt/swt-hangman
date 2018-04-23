import wordgenerator
import sys
from painter.painterfactory import PainterFactory
from utility.consoleoperator import ConsoleOperator
from recorder.base import BaseRecorder

class GameplayController:

    def new_game(self):
        self.selected_letters = []
        self.number_of_fails = 0
        self.max_fails = 8

        self.painter = PainterFactory().get_painter(self.max_fails)

        self.word_generator = wordgenerator.get('plaintext')
        self.word = self.word_generator.get_word_with_filename('default')
        BaseRecorder().word = self.word.word

        self.run_game()

    def run_game(self):
        print("Guess the word: ")
        self.painter.display_masked_word(self.selected_letters, self.word.characters)

        while not self.has_guessed_word():
            letter_input = input('Insert letter: ') # Request user input
            letter_input = letter_input.lower().strip() # Format input, trim and convert to lowercase

            # If the input is not valid
            if not self.validate_input(letter_input):
                continue

            # Check if the letter has already been entered by the user
            if self.has_used_letter(letter_input):
                print("The letter has already been used! {}".format(self.selected_letters))
                print("You made {} mistakes".format(self.number_of_fails))
            else:
                ConsoleOperator().clear_console()

                # Add the new letter to the list of used letters
                self.selected_letters.append(letter_input)

                self.update_number_of_fails(letter_input)

                BaseRecorder().selected_letters = self.selected_letters
                self.painter.draw_current_state(self.number_of_fails)
                print("Selected letters: {}, your total amount of mistakes: {}/{}".format(self.selected_letters, self.number_of_fails, self.max_fails))

                # Should be replaced by recorder method
                self.painter.display_masked_word(self.selected_letters, self.word.characters)

        # You win the game
        print("Well done! You have {} number of fails...".format(self.number_of_fails))
        self.record(1)
        self.request_replay()

    def validate_input(self, user_input):
        # If the length isnt 1 and the input is not a letter the input is not valid
        if len(user_input) is not 1 or not user_input.isalpha():
            print("Your input is not valid, please input one letter [a-z]")
            return False
        return True


    def request_replay(self):
        cont = input("do you want to continue? (y/n): ")
        if cont == 'y':
            self.new_game()
        elif cont == 'n':
            sys.exit()
            return
        else:
            print('Please enter y or n!')

    # Method which is called if player does not guess the word within allowed number of tries
    def game_over(self):
        self.record(0)
        self.painter.draw_lose_state(self.word.word)
        self.request_replay()

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
        if  self.number_of_fails == self.max_fails:
            self.game_over()

    # Recorder saves to text
    def record(self, win):
        score = BaseRecorder().calculate_score(self.word.word, len(self.selected_letters), self.number_of_fails, win)
        BaseRecorder().write_to_text(score, win)