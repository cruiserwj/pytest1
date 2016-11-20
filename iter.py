class CurckIteration(object):
    def __init__(self):
        self.a = 0

    def __iter__(self):
        return self

    def next(self):
        self.a += 1
        if self.a >100:
            raise StopIteration()
        return self.a


for n in CurckIteration():
    print n

