import threading
from threading import Thread
from testMine import *

class AlmostClockChain(threading.Thread):
    def __init__(self, name, difficulty):
        threading.Thread.__init__(self)
        self.name = name
        self.difficulty = difficulty

    def run(self):
        print("Starting thread "+self.name+"\n")
        tm = TestMine(self.difficulty)
        
t1=AlmostClockChain("Non-RPI_1",5)
t2=AlmostClockChain("Non-RPI_2",3)

t1.start()
t2.start()

t1.join()
t2.join()
