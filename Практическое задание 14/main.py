import time
def nTime(prg):
    def pogtime(*args):
        st = time.time()
        prg(*args)
        ct= time.time() - st
        print(ct)
        return True
    return pogtime


def spisok1(n):
    def start1():
        s = list()
        for i in range(0, n + 1):
            if i % 2 == 0:
                s.append(i)
                return s
    return spisok1

def spisok2(n):
    def start1():
        s=[int(i) for i in range(0,n+1) if i%2 == 0]
        return s
    return spisok2

s = nTime(spisok1)
c = nTime(spisok2)
s(1000)
c(1000)