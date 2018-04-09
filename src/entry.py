from controller.base import BaseController
import sys

if __name__ == "__main__":
    controller = BaseController(sys.argv[1:])
    controller.start()
