from threading import Timer
from time import sleep
from datetime import datetime
import sys
import ping

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


class Environment():
    def __init__(self, ip_adress, status=True):
        self.ip = ip_adress
        self.status = status
    
    def set_status(self, status):
        if not status == self.status:
            print("STATUS CHANGED!")
            if status == False:
                print("DOWN")
            else:
                print("UP")
        else:
            print(f'Enviromet Status: {status}')

if __name__ == '__main__':
    env = Environment("127.0.0.1")
    r = RepeatingTimer(ping.ping_at, 20, env)
    r.start()
