from abc import ABCMeta, abstractmethod

class programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):

        return "yes"

class Python(programming):

    def has_oop(self):

        return "yes"

class Pascal(programming):

    def has_oop(self):

        return "No"

one = Pascal()
print(one.has_oop())