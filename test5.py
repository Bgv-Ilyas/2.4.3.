from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
        pass
