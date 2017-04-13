import multiprocessing, time, threading
from urllib import request

def run(name):
    print("name--%s" % name)
    time.sleep(2)

def f(url):
    q = request.urlopen(url)
    data = q.read()
    print('%d bits recv from %s' % (len(data), url))

if __name__ == "__main__":
    start = time.time()
    #for i in range(10):
        #t = threading.Thread(target=run, args=("hhhhs%s" % i,))
    #    p = multiprocessing.Process(target=run, args=("hha%s" % i,))
    #    p.start()
    urls = ['https://www.python.org/', 'https://yahoo.com', 'https://github.com']
    for url in urls:
        p = threading.Thread(target=f, args=("%s" % url,))
        p.start()
    p.join()
    print(time.time()-start)