from client.infrastructure.settings.settings import Settings
from structured_logging.configuration.environment import Environment
from structured_logging.processors.abstract_processor import AbstractProcessor


class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, environment: Environment) -> None:
        self._environment = environment
    
    _next: AbstractProcessor

    def handle(self, data: dict):
        data['environment']: Environment = self._environment
        super().handle(data)