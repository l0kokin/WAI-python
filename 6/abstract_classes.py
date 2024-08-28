from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def say_hi(self):
        pass


class French(Human):
    def say_hi(self):
        print('Salut')


class Georgian(Human):
    def say_hi(self):
        print('Gamarjoba')


human1 = French('Sam', 25)
human1.say_hi()
human2 = Georgian('Sali', 27)
human2.say_hi()