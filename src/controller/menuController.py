import sys
from controller.gameplayController import GameplayController

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
        if option == 1:
            game = GameplayController()
            game.new_game()
        
        if option == 2:
            # Initiate game explanation class
            print("This option is not yet implemented")
            sys.exit
        
        if option == 3:
            # Initiate highscore class 
            print("This option is not yet implemented")
            sys.exit

    def check_int(self, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()