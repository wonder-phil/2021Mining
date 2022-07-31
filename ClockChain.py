import threading
from threading import Thread
from RPI_Mine import *

class ClockChain(threading.Thread):
    def __init__(self, port, name, difficulty):
        threading.Thread.__init__(self)
        self.port = port
        self.name = name
        self.difficulty = difficulty
        self._return = None

    def run(self):
        print("Starting thread "+self.name+"\n")
        rpi_mine = RPI_Mine(int(self.port), self.name, self.difficulty)
        self._return = rpi_mine.return_value()

    def join(self):
        Thread.join(self)
        return self._return        
        
t1=ClockChain(5022,"RPI_1",4)
t2=ClockChain(5023,"RPI_2",4)

t2.start()
t1.start()


x = t1.join()
y = t2.join()

print("x: ",x,"y: ",y)
