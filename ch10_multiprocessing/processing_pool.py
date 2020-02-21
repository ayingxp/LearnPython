# -*- coding: utf-8 -*-

from multiprocessing import Process, Pool

import time

def Foo(i):
    time.sleep(2)
    print 'in process: ', i
    return i + 100

def Bar(arg):
    print '--->exec done:', arg



if __name__ == '__main__':
    pool = Pool(5)

    for i in range(10):
        #pool.apply_async(func=Foo, args=(i,), callback=Bar) # 异步必行
        pool.apply(func=Foo, args=(i,)) # 串行运行

    print 'end'
    pool.close()
    pool.join()  # 等待进程运行结束，如果没有此行，则程序没等所有进程运行完成就退出

