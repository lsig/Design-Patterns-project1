from typing import List
from structured_logging.processors.I_processor import IProcessor
from structured_logging.processors.abstract_processor import AbstractProcessor


class MaskingProcessor(AbstractProcessor):
    def __init__(self, masks: List) -> None:
        self._masks = masks
        self._masker = "***"
    
    def handle(self, data: dict):
        data = self.check_keys_recursive(data)
        return super().handle(data)


    def check_keys_recursive(self, data: dict) -> dict:
        for key in data.keys():
            already_masked = False
            for mask in self._masks:

                if key == mask:
                    already_masked = True
                    data[key] = self._masker
                
            if not already_masked and isinstance(data[key], dict):
                data[key] = self.check_keys_recursive(data[key])
        
        return data
                