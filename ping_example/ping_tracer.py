from threading import Timer, Thread
from datetime import datetime

class PT():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

def printer():
    tempo = datetime.today()
    h,m,s = tempo.hour, tempo.minute, tempo.second
    print(f"{h}:{m}:{s}")


t = PT(1, printer)
t.start()
