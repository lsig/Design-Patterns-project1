from client.infrastructure.logging.I_logger import ILogger
from structured_logging.logger.logger import Logger
from structured_logging.sinks.I_sink import ISink

class ClientLogger(ILogger): 
    def __init__(self, external_logger: Logger) -> None:
        self.__external_logger = external_logger

    def error(self, message: str, exception: Exception = None):
        data = dict()
        data['message'] = message
        data['level'] = 'error'
        data['exception'] = exception

        self.__external_logger.log(data=data)
        
    def warning(self, message: str, exception: Exception = None):
        data = dict()
        data['message'] = message
        data['level'] = 'warning'
        data['exception'] = exception

        self.__external_logger.log(data=data)


    def info(self, message: str):
        data = dict()
        data['message'] = message
        data['level'] = 'info'

        self.__external_logger.log(data=data)
        