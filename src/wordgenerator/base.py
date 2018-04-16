from abc import ABCMeta, abstractmethod

class BaseWordGenerator(metaclass=ABCMeta):

    @abstractmethod
    def get_word(self):
        pass

    @abstractmethod
    def generate_words(self):
        pass