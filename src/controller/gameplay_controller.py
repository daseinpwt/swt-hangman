from abc import ABCMeta, abstractmethod

class Gameplay_Controller(metaclass=ABCMeta):

	@abstractmethod
	def new_game(self):
		pass

	@abstractmethod
	def run_game(self):
		pass