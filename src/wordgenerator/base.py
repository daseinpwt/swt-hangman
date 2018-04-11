from abc import ABCMeta, abstractmethod

class BaseWordGenerator:

    @abstractmethod
    def get_word(self):
        pass

    @abstractmethod
    def generate_words(self, filename = ""):
    	pass

