from structured_logging.processors.abstract_processor import AbstractProcessor

class NullProcessor(AbstractProcessor):
    def handle(self, data: dict):
        super().handle(data)