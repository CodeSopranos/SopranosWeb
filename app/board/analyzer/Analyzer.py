import abc as ABC
from abc import ABC, abstractmethod, abstractproperty


class Analyzer(ABC):

    @abstractmethod
    def analyze(self):
        pass
