from structured_logging.processors.abstract_processor import AbstractProcessor
from structured_logging.processors.I_processor import IProcessor

class NullProcessor(AbstractProcessor):
    _next: AbstractProcessor

    def set_next(self, processor: IProcessor):
        self._next = processor

    def handle(self, data: dict):
        return super().handle(data)