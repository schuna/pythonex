from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bow Bow!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!")


class ForestFactory(object):
    @staticmethod
    def make_sound(object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    ff.make_sound("Dog")
    ff.make_sound("Cat")
