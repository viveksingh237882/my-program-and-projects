import time
from functiontools import lru_cache





@cache(maxsize=3)
def some_work(n):
    time .sleep=n
    return (n)
if __name__=="__main__":
    print('now running  time ')
    some_work(3)
    print('We are now do our work within sometime')
    some_work(3)
    print('called again')
    some_work(3)
    print('called again')
    some_work(3)
    print('called again')
     



