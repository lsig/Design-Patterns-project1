from structured_logging.sinks.I_sink import ISink
from json import dumps

class FileSink(ISink):
    def __init__(self, filepath: str) -> None:
        self._filepath = filepath

    def sink_data(self, data: dict):
        self._json_object = dumps(data, indent=4)
        self.log_data()

    def log_data(self):
        with open(self._filepath, 'a') as file:
            file.write(self._json_object)


