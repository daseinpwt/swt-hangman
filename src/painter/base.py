class BasePainter:

    def __init__(self, mask):
        self.mask = mask

    def draw_current_state(self, numFails):
        print()
        if numFails == 0:
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')

        elif numFails == 1:
            print('..-------..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')

        elif numFails == 2:
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')

        elif numFails == 3:
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('....|...|..')
            print('....|...|..')
            print('........|..')
            print('........|..')

        elif numFails == 4:
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('....|/..|..')
            print('....|...|..')
            print('........|..')
            print('........|..')

        elif numFails == 5:
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('...\\|/..|..')
            print('....|...|..')
            print('........|..')
            print('........|..')

        elif numFails == 6:
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('...\\|/..|..')
            print('....|...|..')
            print('.....\\..|..')
            print('........|..')

        elif numFails == 7:
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('...\\|/..|..')
            print('....|...|..')
            print('.../.\\..|..')
            print('........|..')
        print()

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
        print('....|...|..')
        print('....X...|..')
        print('...\\|/..|..')
        print('....|...|..')
        print('.../.\\..|..')
        print('........|..')
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