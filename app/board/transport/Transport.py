import abc as ABC
from abc import ABC, abstractmethod, abstractproperty


class Transport(ABC):

    @abstractmethod
    def get(self, tag, **params):
        pass

