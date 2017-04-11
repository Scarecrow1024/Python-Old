import threading

class MyThread(threading.Thread):
    def __init__(self, n):
        self.n = n
        super(MyThread, self).__init__()

    def run(self):
        print('run task', self.n)

t1 = MyThread('t1')
t2 = MyThread('t2')

t1.start()
t2.start()