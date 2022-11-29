from abc import ABC, abstractmethod

class Car():
    @abstractmethod
    def do_something(self):
        print("Car is faster than bike")
        