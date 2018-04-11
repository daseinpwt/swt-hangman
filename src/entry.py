import sys
from controller.singleplayerController import SingleplayerController

if __name__ == '__main__':
    gameplay_controller = SingleplayerController()
    gameplay_controller.new_game()
    gameplay_controller.run_game()