from time import sleep
from typing import List
from structured_logging.command_queue.command import Command
import threading

from structured_logging.configuration.logger_config import LoggerConfig


class Node:
    def __init__(self, value: Command = None, next: 'Node' = None, prev: 'Node' = None) -> None:
        self.value = value
        self.next = next  
        self.prev = prev


class Queue:
    def __init__(self, config: LoggerConfig):

        self.__head = Node(value=None)
        self.__tail = Node(value=None, next=self.__head)
        self.__head.prev = self.__tail
        self.__size = 0

        self.__delay: int = config.async_wait_delay_in_seconds

        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()


    def add(self, command: Command):
        newNode = Node(value=command, next=self.__tail.next, prev=self.__tail)
        
        self.__tail.next.prev = newNode
        self.__tail.next = newNode
        self.__size += 1


    def pop(self):
        firstNode = self.__head.prev

        self.__head.prev.prev.next = self.__head
        self.__head.prev = self.__head.prev.prev

        self.__size -= 1

        return firstNode.value


    def __process(self):
        while (True):
            if self.__size > 0:
                self.pop().execute()
            else:
                sleep(self.__delay)
