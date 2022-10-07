from abc import abstractmethod
from structured_logging.processors.I_processor import IProcessor


class AbstractProcessor(IProcessor):
    _next: 'AbstractProcessor'

    def set_next(self, processor: IProcessor):
        self._next = processor
        return processor


    @abstractmethod
    def handle(self, data: dict):
        if (self._next != None):
            self._next.handle(data)