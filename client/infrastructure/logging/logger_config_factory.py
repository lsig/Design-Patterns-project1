from client.infrastructure.settings.settings import LoggingType, Settings
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder
from structured_logging.processors.timestamp_processor import TimestampProcessor


def create_logger_config(settings: Settings) -> LoggerConfig:
        builder = LoggerConfigBuilder().add_environment(settings.environment).add_processor(TimestampProcessor())

        if settings.logging_is_async:
            builder.as_async(settings.logging_async_delay)

        if settings.logging_type == LoggingType.CONSOLE:
            builder.with_console_sink()

        elif settings.logging_type == LoggingType.FILE:
            builder.with_file_sink(settings.logging_file_path)


        return builder.build()