from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print 'task name:%s (%s)' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'task %s lasted %0.2f s' % (name, (end - start))


if __name__ == '__main__':
    print 'father is %s' % os.getpid()
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'wait'
    p.close()
    p.join()
    print 'done'
