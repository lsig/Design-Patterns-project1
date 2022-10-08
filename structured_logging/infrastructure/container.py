from dependency_injector import containers, providers
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logger import Logger
from structured_logging.processors.null_processor import NullProcessor
from structured_logging.sinks.console_sink import ConsoleSink




class Container(containers.DeclarativeContainer):
        config: LoggerConfig = providers.Configuration()

        logger = providers.Singleton(Logger,
                                logger_config=config,
                                logging_queue=Queue(config.async_wait_delay_in_seconds)
                            )