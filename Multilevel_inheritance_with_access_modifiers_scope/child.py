
from sub_class import *

class Aspirant(Student):
 
       # constructor
       def __init__(self, name,course,roll):
            Student.__init__(self, name,course,roll)
         
       # public member function
       def displayDetails(self):    
             # accessing protected data members of parent class
            print("Name: ", self._name)

             # accessing protected member functions of super class
            self._displayRollAndCourse()