import threading
from threading import Thread
from RPI_Mine import *

class ClockChain(threading.Thread):
    def __init__(self, port, name, difficulty):
        threading.Thread.__init__(self)
        self.port = port
        self.name = name
        self.difficulty = difficulty

    def run(self):
        print("Starting thread "+self.name+"\n")
        tm = RPI_Mine(int(self.port), self.name, self.difficulty)
        
t1=ClockChain(5022,"RPI_1",4)
t2=ClockChain(5023,"RPI_2",2)

t1.start()
t2.start()

t1.join()
t2.join()
