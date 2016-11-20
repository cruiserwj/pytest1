#!/user/bin/env python
import sys

def test():
    a = sys.argv
    if len(a) == 1:
        print 'hello world'
    elif len(a) ==2:
        print 'hello %s'%a[1]
    else:
        print 'Much more agurements'

if __name__ == '__main__':
    test()
