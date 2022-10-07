from structured_logging.command_queue.command import Command
from structured_logging.sinks.I_sink import ISink


class LoggingCommand(Command):
    def __init__(self, sink: ISink, data: dict) -> None:
        self.__sink = sink
        self.__data = data

    def execute(self):
        self.__sink.sink_data(self.__data)