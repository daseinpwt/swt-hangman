from abc import ABCMeta, abstractmethod

class BaseWordGenerator:

    def __init__(self):
        pass

    @abstractmethod
    def getWord(self):
        pass
