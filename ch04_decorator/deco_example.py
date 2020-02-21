# -*- coding: utf-8 -*-

import time

def timer(func):
    start = time.time()
    def deco(*args):
        #start_time = time.time()
        return func(*args)
        #stop_time = time.time()
        #print 'the func run time is %s' % (stop_time - start_time)
    end = time.time()
    print 'the func run time is %s' % (end - start)
    return deco


@timer # test1 = timer(test1)
def test1():
    print 'in func test1'

@timer
def calc(x, y):
    return  x + y




test1()
res = calc(8,9)

print '****'*20
print res


print res



