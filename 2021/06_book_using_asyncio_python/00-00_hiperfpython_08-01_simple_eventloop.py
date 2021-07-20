from queue import Queue
from functools import partial
from time import sleep


eventloop = None


class EventLoop(Queue):
    count = 50

    def start(self):
        while True:
            function = self.get()
            function()
            self.count -= 1
            sleep(0)
            if self.count == 0:
                break

    def end(self):
        self.count = 0


def do_hello():
    global eventloop
    print("Hello")
    eventloop.put(do_world)


def do_world():
    global eventloop
    print("world")
    eventloop.put(do_hello)


if __name__ == "__main__":
    eventloop = EventLoop()
    eventloop.put(do_hello)
    eventloop.start()
    # sleep(1.0)
    # eventloop.end()
