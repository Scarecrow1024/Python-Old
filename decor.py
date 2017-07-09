def log(func):
    def wrapper(*args, **kw):
        print('call %s' %func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2017-07-08')

if __name__=='__main__':
    now()
