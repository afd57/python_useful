from threading import Timer
from time import sleep
from datetime import datetime


class RepeatingTimer():
    """
    USAGE:
    from time import sleep
    r = RepeatingTimer(_print, 0.5, "hello")
    r.start(); sleep(2); r.interval = 0.05; sleep(2); r.stop()
    """

    def __init__(self, function, interval, *args, **kwargs):
        super(RepeatingTimer, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.function = function
        self.interval = interval

    def start(self):
        self.callback()
	
    def stop(self):
        self.interval = False
	
    def callback(self):
        if self.interval:
            self.function(*self.args, **self.kwargs)
            Timer(self.interval, self.callback, ).start()


def printer():
    tempo = datetime.today()
    h,m,s = tempo.hour, tempo.minute, tempo.second
    print(f"{h}:{m}:{s}")


def _print(arg):
    printer()
    sleep(5)

if __name__ == '__main__':
    print('hello')
    r = RepeatingTimer(_print, 1.0, "hello")
    r.start()
