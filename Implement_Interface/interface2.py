from interface import *

class MyClass(MyInterface):

    # Overriding abstract method of Interface ::
    def absmethod(self):
        print("Method overridden from Interface...")