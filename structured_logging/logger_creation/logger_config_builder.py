from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.I_processor import IProcessor
from structured_logging.sinks.I_sink import ISink
from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.sinks.file_sink import FileSink
from structured_logging.processors.environment_processor import EnvironmentProcessor
from structured_logging.processors.null_processor import NullProcessor


class LoggerConfigBuilder:
    def __init__(self):
        self._clear()

    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        self.__logger.sink = sink
        return self

    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        self.__logger.sink = FileSink(file_path)
        return self

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        self.__logger.sink = ConsoleSink()
        return self

    def as_async(self, wait_delay_in_seconds: int) -> 'LoggerConfigBuilder':
        self.__logger.is_async = True
        self.__logger.async_wait_delay_in_seconds = wait_delay_in_seconds
        return self

    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        self.add_processor(EnvironmentProcessor(environment))
        return self

    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        processor.set_next(self.__logger.processor)
        self.__logger.processor = processor

        return self

    def _clear(self):
        self.__logger = LoggerConfig(
            sink=ConsoleSink(), 
            processor=NullProcessor(), 
            is_async=False, 
            async_wait_delay_in_seconds=0)

    def build(self) -> LoggerConfig:
        logger = self.__logger
        self._clear()
        return logger

  