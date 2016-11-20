import threading,thread
import time

def loop():
    print 't %s is running' % threading.current_thread().name
    n =0
    while n < 5 :
        n +=1
        print  't %s >>>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 't %s is end' % threading.current_thread().name

print 't %s is running' %  threading.current_thread().name

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 't %s is end' % threading.current_thread().name
