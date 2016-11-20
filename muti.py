from multiprocessing import Process
import os
def run_proc(name):
    print 'name:%s (%s)' % (name,os.getpid())

if __name__ == '__main__':
    print 'father is %s' % os.getpid()
    p= Process(target=run_proc,args=('test',))
    print 'will start'
    p.start()
    p.join()
    print 'the end'