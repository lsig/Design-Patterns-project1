from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.I_processor import IProcessor
from structured_logging.sinks.I_sink import ISink
from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.sinks.file_sink import FileSink


class LoggerConfigBuilder:
    def __init__(self):
        self._clear()

    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        self.__logger.sink = sink

    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        self.__logger.sink = FileSink(file_path)

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        self.__logger.sink = ConsoleSink()

    def as_async(self, wait_delay_in_seconds: int) -> 'LoggerConfigBuilder':
        self.__logger.async_wait_delay_in_seconds = wait_delay_in_seconds

    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        raise NotImplementedError()

    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        self.__logger.processor = processor

    def _clear(self):
        self.__logger = LoggerConfig()

    def build(self) -> LoggerConfig:
        self._clear()
        return self.__logger

  