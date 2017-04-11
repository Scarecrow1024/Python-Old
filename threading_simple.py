import threading
import time

num = 0
def run2():
    lock.acquire()
    global num
    num += 1
    lock.release()

lock = threading.Lock()

for i in range(100):
    tt = threading.Thread(target=run2)
    tt.start()
print("num:", num)

def run(n):
    print(n)
    time.sleep(2)
start_time = time.time()
ts = []
for i in range(50):
    t = threading.Thread(target=run, args=('t--%s' % i,))
    t.start()
    ts.append(t)
for t in ts:
    t.join()

print('done', time.time()-start_time)
