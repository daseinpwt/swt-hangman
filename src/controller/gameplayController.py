from abc import ABCMeta, abstractmethod

class GameplayController(metaclass=ABCMeta):

    @abstractmethod
    def new_game(self):
        pass

    @abstractmethod
    def run_game(self):
        pass