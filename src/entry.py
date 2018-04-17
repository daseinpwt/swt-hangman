import sys
from controller.singleplayerController import SingleplayerController
from controller.replayController import ReplayController

if __name__ == '__main__':
    gameplay_controller = ReplayController()
    gameplay_controller.new_game()
