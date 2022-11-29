from abc import ABC, abstractmethod

class MyInterface(ABC):
    # Defining abstract method ::
    @abstractmethod
    def absmethod(self):
        pass