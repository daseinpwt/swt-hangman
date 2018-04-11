from abc import ABCMeta, abstractmethod

class BaseWordGenerator:

    def __init__(self):
        pass

    @abstractmethod
    def get_word(self):
        pass

    @abstractmethod
    def generate_words(self):
    	pass