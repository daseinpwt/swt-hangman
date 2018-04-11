class BasePainter:
    def __init__(self, max_num_fails):
        self.max_num_fails = max_num_fails

    def draw_current_state(self, guess, word, num_fails):
        print()
        print('-----O-----')
        print('----\\|/----')
        print('-----|-----')
        print('----/ \\----')
        print('The word:\n\t', end = '')
        for i, c in enumerate(word):
            if guess[i]:
                print(c, end = '')
            else:
                print('_', end = '')
        print()
        print()

    def draw_win_state(self, word, num_fails):
        print()
        print('Congratulations! You win!')
        print('The word is:\n\t', end = '')
        print(word)
        print()

    def draw_lose_state(self, guess, word):
        print()
        print('-----X-----')
        print('----\\|~----')
        print('-----|-----')
        print('----< \\----')
        print('You Lose!')
        print('The word is:\n\t', end = '')
        print(word)
        print()

    def get_new_guess(self):
        return input('Please guess a new character: ')
