import time
def testTime(fn):
    def wrapper(a, n, proFibon):
        st = time.time()
        y = fn(a, n, proFibon)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")
        return y
    return wrapper

def Fibon(n):
    a = 0
    s = list()
    while a <= n:
        if len(s) == 0:
            s.append(0)
            s.append(1)
        else:
            a = s[-1]+s[-2]
            if a <= n:
                s.append(a)
            else:
                break
    return s

def proFibon(s,n):
    while s[-1]+s[-2] <= n:
        a = s[-1] + s[-2]
        if a <= n:
            s.append(a)
        else:
            break
    return s
@testTime
def info(fn,n,proFib):
    def getinfo():
        s = []
        if fn[-1] + fn[-2] < n:
            while fn[-1] + fn[-2] < n:
                s = proFib(fn,n)
        else:
            for i in range(len(fn)):
                if n > fn[i]:
                    s.append(fn[i])
        return s
    return getinfo()

a = Fibon(5)
n = 100
b = info(a, n, proFibon)
print(b)

