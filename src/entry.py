import sys
from controller.singleplayerController import SingleplayerController
from controller.replayController import ReplayController
from controller.baseController import BaseController

if __name__ == '__main__':
    gameplay_controller = SingleplayerController()
    gameplay_controller.new_game()
