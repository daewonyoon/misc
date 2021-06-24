import threading
from queue import Queue


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == "prepare table":
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == "clear table":
                self.cutlery.give(to=kitchen, knives=4, forks=4)

            elif task == "shutdown":
                return


from attr import attrs, attrib


@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: "Cutlery", knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


kitchen = Cutlery(knives=100, forks=100)
bots = [ThreadBot() for i in range(10)]


import sys

for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put("prepare table")
        bot.tasks.put("clear table")
    bot.tasks.put("shutdown")

print("Kitchen inventory before service: ", kitchen)
for bot in bots:
    bot.start()

for bot in bots:
    bot.join()
print("Kitchen inventory after service: ", kitchen)



""" 
(v3864) C:\D\github\daewonyoon\misc\2021\06_book_using_asyncio_python>python 02-03_bot_cutlery.py 100
Kitchen inventory before service:  Cutlery(knives=100, forks=100)
Kitchen inventory after service:  Cutlery(knives=100, forks=100)

(v3864) C:\D\github\daewonyoon\misc\2021\06_book_using_asyncio_python>python 02-03_bot_cutlery.py 10000
Kitchen inventory before service:  Cutlery(knives=100, forks=100)
Kitchen inventory after service:  Cutlery(knives=100, forks=104)

(v3864) C:\D\github\daewonyoon\misc\2021\06_book_using_asyncio_python>python 02-03_bot_cutlery.py 100000
Kitchen inventory before service:  Cutlery(knives=100, forks=100)
Kitchen inventory after service:  Cutlery(knives=92, forks=100)
"""