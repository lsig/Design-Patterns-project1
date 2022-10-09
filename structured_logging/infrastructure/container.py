from dependency_injector import containers, providers
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logger import Logger

class Container(containers.DeclarativeContainer):
        config: LoggerConfig = providers.Configuration()

        __queue_provider = providers.Singleton(Queue, config=config)

        logger = providers.Singleton(Logger,
                                logger_config=config,
                                logging_queue=__queue_provider)
