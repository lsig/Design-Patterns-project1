from abc import ABC, abstractmethod

from client.models.payment import Payment


class ILogger(ABC):
    @abstractmethod
    def error(self, message: str, exception: Exception = None):
        pass

    @abstractmethod
    def warning(self, message: str, exception: Exception = None):
        pass

    @abstractmethod
    def info(self, message: str):
        pass

    @abstractmethod
    def payment(self, payment: Payment):
        pass