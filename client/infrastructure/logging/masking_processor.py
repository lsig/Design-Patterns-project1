from typing import List
from structured_logging.processors.I_processor import IProcessor
from structured_logging.processors.abstract_processor import AbstractProcessor


class MaskingProcessor(AbstractProcessor):
    def __init__(self, masks: List) -> None:
        self._masks = masks
    
    def handle(self, data: dict):
        for mask in self._masks:
            if data.get(mask):
                data[mask] = "***"

        return super().handle(data)
