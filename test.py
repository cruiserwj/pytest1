class stu(object):
    def __init__(self,name='a',score=0):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s:%s'%(self.__name,self.__score)


class xiaoming(stu):
    def __init__(self,age=0):
        self.__age =age

    def print_score(self):
        print 'xiaoming is %s' %self.__age

class xiaohong(stu):
    def __init__(self,sex):
        self.__sex = sex

def print2(stu):
    stu.print_score()
    stu.print_score()
xiaoming(12).print_score()
print2(xiaoming())


