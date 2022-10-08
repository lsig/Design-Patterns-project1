from client.infrastructure.settings.settings import Settings
from structured_logging.configuration.environment import Environment
from structured_logging.processors.abstract_processor import AbstractProcessor


class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, environment: Environment) -> None:
        self._environment = environment
    

    def handle(self, data: dict):
        data['environment']: str = self._environment.name
        super().handle(data)