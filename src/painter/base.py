class BasePainter:
    def __init__(self, maxNumFails):
        self.maxNumFails = maxNumFails

    def drawCurrentState(self, guess, word, numFails):
        if numFails > 0:
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

    def drawWinState(self, word, numFails):
        print()
        print('Congratulations! You win!')
        print('The word is:\n\t', end = '')
        print(word)
        print()

    def drawLoseState(self, guess, word):
        print()
        print('-----X-----')
        print('----\\|~----')
        print('-----|-----')
        print('----< \\----')
        print('You Lose!')
        print('The word is:\n\t', end = '')
        print(word)
        print()

    def getNewGuess(self):
        return input('Please guess a new character: ')
