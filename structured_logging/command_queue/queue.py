from time import sleep
from typing import List
from structured_logging.command_queue.command import Command
import threading


class Queue:
    def __init__(self, async_delay: int):
        self.__queue: List[Command] = []
        self.__delay = async_delay
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()

    def add(self, command: Command):
        self.__queue.append(command)

    def __process(self):
        while (True):
            if self.__queue == []:
                sleep(self.__delay)
            else:
                self.__queue.pop().execute()



