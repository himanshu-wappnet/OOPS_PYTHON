from parent import *

class Student(Person):
    
    # Private class variables ::
    _roll = None
    _course = None
    
    def __init__(self,name,course,roll):
        Person.__init__(self,name)
        self._course = course
        self._roll = roll
      
    # Private class method ::
    def _displayRollAndCourse(self):
        print("Roll: ", self._roll)
        print("Branch: ", self._course)

