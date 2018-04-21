import sys
from controller.gameplayController import GameplayController
from utility.consoleoperator import ConsoleOperator

class MenuController:

    def __init__(self):
        self.print_menu()
        self.request_input()

    def print_menu(self):
        print('========================')
        print('Welcome to Hangman Game!')
        print('========================')
        print('[1] - Start new game')
        print('[2] - Game explanation')
        print('[3] - Highscores')

    def request_input(self):
        user_input = input("Choose an option: ") # Request user input
        user_input = user_input.strip()

        if self.check_int(user_input):
            if(0 < int(user_input) < 4):
                self.select_option(int(user_input))
                return

        print("You have not selected a valid option, please pick option 1-3")
        self.request_input()

    def select_option(self, option):
        ConsoleOperator().clear_console()

        if option == 1:
            game = GameplayController()
            game.new_game()
        
        if option == 2:
            # Initiate game explanation class
            print("Welcome to hangman...")
            print("Hangman is a word guessing game, where you will be trying to guess the word by suggesting letters")
            print("The words are respresented by a row of dashes, representing each letter of the word")
            print("When correctly guessing a letter which is in the word, the dashes will be replaced by your guessed letter")
            print("However your impending doom comes closer with each wrongly guessed letter")
            print("When you have exhausted all your guesses, you will be hung! \n")
            print("To start the game choose option 1")

            self.print_menu()
            self.request_input()
        
        if option == 3:
            # Initiate highscore class 
            print("This option is not yet implemented")
            self.print_menu()
            self.request_input()
            sys.exit

    def check_int(self, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()