import os

class Person:
    
    # protected and private class variables 
    _name = None
    _age = None
    
    # Using Constructor for filling up name and age of a person.
    def __init__(self,name):
        self._name = name
        self._age = 0
        print("Onboarding started....")
