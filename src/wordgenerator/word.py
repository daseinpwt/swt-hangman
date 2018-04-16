class Word:
    def __init__(self, word):
        self.characters = list(word)

    def display_masked_word(self, selected_letters = []): # Has to be moved to Painter
        display_string = ""
        for letter in self.characters:
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
        for l in self.characters:
            if l == letter:
                letter_in_word = True

        return letter_in_word