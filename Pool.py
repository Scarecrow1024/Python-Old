from multiprocessing import Pool, Process, freeze_support
from urllib import request
import time, os

def foo(i):
    time.sleep(1)
    print(os.getpid())

def f(url):
    q = request.urlopen(url)
    data = q.read()
    print('%d bits recv from %s' % (len(data), url))

if __name__ == "__main__":
    freeze_support()
    pool = Pool(5)
    #for i in range(10):
    #    pool.apply_async(func=foo, args=(i,))
    start = time.time()
    urls = ['https://www.python.org/', 'https://yahoo.com', 'https://github.com']
    for url in urls:
        pool.apply_async(func=f, args=('%s' % url,))
    pool.close()
    pool.join()
    print("chuanxing:", time.time() - start)
    #print("end")