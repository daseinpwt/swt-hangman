class BasePainter:

    def __init__(self, mask):
        self.mask = mask

    def draw_current_state(self, numFails):
        pass

    def draw_win_state(self, word):
        print()
        print('Congratulations! You win!')
        print('The word is:\n\t', end = '')
        print(word)
        print()
        print()
        print('...........')
        print('....YOU....')
        print('....ARE....')
        print('.....A.....')
        print('...CHAMP...')
        print('...........')
        print()

    def draw_lose_state(self, word):
        print()
        print('..-------..')
        print('....|.\\.|..')
        print('....X..\\|..')
        print('...\\|/..|..')
        print('....|...|..')
        print('.../.\\..|..')
        print('........|..')
        print('._________.')
        print('.|.......|.')
        print('You Lose!')
        print('The word is:\n\t', end = '')
        print(word)
        print()

    def display_masked_word(self, selected_letters = [], characters = []):
        display_string = ""
        for letter in characters:
            has_guessed = False

            for guessed_letter in selected_letters:
                if letter == guessed_letter:
                    has_guessed = True

            if has_guessed:
                display_string += " {} ".format(letter)
            else:
                display_string += "{}".format(self.mask)

        print("{}".format(display_string))
