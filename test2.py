from types import MethodType
class myabs(object):
    def __abs__(self):
        return 'Don\'t tell you'

print abs(-100)
print abs(myabs())

obj = myabs()
setattr(obj,'name','wangjue')

print obj.name


def print2(self):
    print 'wooll'

myabs.print2 = MethodType(print2,None,myabs)

o1 = myabs()
o1.print2()