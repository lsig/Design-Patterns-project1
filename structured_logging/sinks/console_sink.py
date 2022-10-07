from structured_logging.sinks.I_sink import ISink
from json import dumps

class ConsoleSink(ISink):
    def sink_data(self, data: dict):
        json_object = dumps(data, indent=4)
        print(json_object)