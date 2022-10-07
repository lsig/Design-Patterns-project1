from structured_logging.processors.abstract_processor import AbstractProcessor
from datetime import datetime

class TimestampProcessor(AbstractProcessor):
    _next: AbstractProcessor

    def handle(self, data: dict):
        data['timestamp'] =  datetime.now()
        super().handle(data)