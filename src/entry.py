import sys
from controller.singleplayer_controller import Singleplayer_Controller

if __name__ == '__main__':
    gameplay_controller = Singleplayer_Controller()
    gameplay_controller.new_game()
    gameplay_controller.run_game()
