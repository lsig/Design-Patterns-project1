from abc import ABC, abstractmethod


class IProcessor(ABC):
    @abstractmethod
    def set_next(self, processor: 'IProcessor'):
        pass


# We decided to make this method explicitly abstract because we want to make sure that implementations add their own functionality to this method.
    @abstractmethod
    def handle(self, data: dict):
        pass

