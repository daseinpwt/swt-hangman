import sys
from controller.base_controller import BaseController
from controller.gameplay_controller import GameplayController
from recorder.base import BaseRecorder

class MenuController(BaseController):

    def start(self):
        self.DIFFICULTY_EASY = 1
        self.DIFFICULTY_NORMAL = 2
        self.DIFFICULTY_HARD = 3

        self.VERSION_NORMAL = 4
        self.VERSION_SPACEMAN = 5

        self.game_difficulty = self.DIFFICULTY_NORMAL # defalut level: normal
        self.game_version = self.VERSION_NORMAL

        self.run()

    def run(self):
        self.clear_console()
        self.request_name()

        while True:
            self.print_menu()
            opt = self.choose_option()
            self.on_option(opt)

    # Method which asks the name of the user (to be used in recorder)
    def request_name(self):
        while True:
            user_input = input("Please enter your name: ")
            user_input = user_input.strip()
            if len(user_input) > 0:
                break
            print("Your name probably a bit longer :) ?")

        BaseRecorder().name = user_input

    def print_welcome_msg(self):
        welcome_msg = "Welcome to Hangman Game, %s!" % BaseRecorder().name
        print('=' * len(welcome_msg))
        print(welcome_msg)
        print('=' * len(welcome_msg))

    def get_difficulty_str(self):
        if self.game_difficulty == self.DIFFICULTY_EASY:
            return 'Easy (12 trials)'
        elif self.game_difficulty == self.DIFFICULTY_NORMAL:
            return 'Normal (8 trials)'
        elif self.game_difficulty == self.DIFFICULTY_HARD:
            return 'Hard (6 trials)'
        else:
            sys.exit(1)

    def get_version_str(self):
        if self.game_version == self.VERSION_NORMAL:
            return 'Normal'
        elif self.game_version == self.VERSION_SPACEMAN:
            return 'Spaceman'
        else:
            sys.exit(1)

    def print_menu(self):
        self.print_welcome_msg()
        print('[1] - Start new game')
        print("      Difficulty: %s" % self.get_difficulty_str())
        print("      Version: %s" % self.get_version_str())
        print('[2] - Game explanation')
        print('[3] - Highscores')
        print('[4] - Options')
        print('[5] - Exit')

    def choose_option(self):
        while True:
            user_input = input("Choose an option: ") # Request user input
            user_input = user_input.strip()
            user_input = int(user_input) if self.check_int(user_input) else None
            if user_input is not None and user_input in range(1, 6):
                break

            print("You have not selected an invalid option, please pick option 1-5")

        return user_input

    def selected_mark(self, expr):
        if expr:
            return ' *'
        else:
            return ''

    def on_option(self, option):
        if option == 1:
            game = GameplayController()
            if self.game_difficulty == self.DIFFICULTY_EASY:
                max_fails = 12
            elif self.game_difficulty == self.DIFFICULTY_NORMAL:
                max_fails = 8
            elif self.game_difficulty == self.DIFFICULTY_HARD:
                max_fails = 6
            else:
                sys.exit(1)

            if self.game_version == self.VERSION_NORMAL:
                variant = 1
            elif self.game_version == self.VERSION_SPACEMAN:
                variant = 2
            else:
                sys.exit(1)

            game.new_game(max_fails, variant)
            self.clear_console()

        elif option == 2:
            self.clear_console()
            # Initiate game explanation class
            print("Welcome to hangman...")
            print("Hangman is a word guessing game, where you will be trying to guess the word by suggesting letters")
            print("The words are respresented by a row of dashes, representing each letter of the word")
            print("When correctly guessing a letter which is in the word, the dashes will be replaced by your guessed letter")
            print("However your impending doom comes closer with each wrongly guessed letter")
            print("When you have exhausted all your guesses, you will be hung!")
            print()
            print("To start the game choose option 1.")
            print("To set the difficulty level and graph version choose option 4.")
            print()

        elif option == 3:
            # Initiate highscore class
            self.clear_console()
            BaseRecorder().show_highscores()

        elif option == 4:
            # Choose options for different games
            while True:
                self.clear_console()
                self.print_welcome_msg()
                print('Difficulty settings:')
                if self.game_version == self.VERSION_NORMAL:
                    print('[1] - Easy Game, 12 trials' +\
                        self.selected_mark(self.game_difficulty == self.DIFFICULTY_EASY))
                else:
                    print()
                print('[2] - Normal Game, 8 trials' +\
                    self.selected_mark(self.game_difficulty == self.DIFFICULTY_NORMAL))
                if self.game_version == self.VERSION_NORMAL:
                    print('[3] - Hard Game, 6 trials' +\
                        self.selected_mark(self.game_difficulty == self.DIFFICULTY_HARD))
                else:
                    print()
                print('Version settings:')
                print('[4] - Normal' +\
                    self.selected_mark(self.game_version == self.VERSION_NORMAL))
                print('[5] - Spaceman' +\
                    self.selected_mark(self.game_version == self.VERSION_SPACEMAN))
                print()
                print('[6] - Return')

                if self.game_version == self.VERSION_NORMAL:
                    set = self.choose_setting([1, 2, 3, 4, 5, 6])
                else:
                    set = self.choose_setting([2, 4, 5, 6])

                if set == 6:
                    self.clear_console()
                    break

        elif option == 5:
            print()
            print('Good Bye. Have a nice day :)')
            sys.exit(0)

    def choose_setting(self, avail_opts):
        while True:
            user_input = input("Choose an option: ") # Request user input
            user_input = user_input.strip()

            user_input = int(user_input) if self.check_int(user_input) else None
            if user_input is not None and user_input in avail_opts:
                break

            print("You have not selected an invalid option, please pick option in %s" % avail_opts)

        if user_input < 4:
            self.game_difficulty = user_input
        elif user_input < 6:
            self.game_version = user_input
            if self.game_version == self.VERSION_SPACEMAN:
                self.game_difficulty = self.DIFFICULTY_NORMAL
        return user_input

    def check_int(self, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()
