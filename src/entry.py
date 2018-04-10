from gameController.base import GameController
import sys

if __name__ == '__main__':
    game = GameController(sys.argv[1:])
    game.new_game()
