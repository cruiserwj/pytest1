import sys,os
def test():
    a = sys.argv[1]
    print a
    str = [x for x in os.listdir('.')]
    def search(s):
        if a in s:
            return True
        else:
            return False
    print filter(search,str)


if __name__ == '__main__':
    test()
