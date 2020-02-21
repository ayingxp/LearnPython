# -*- coding: utf-8 -*-

import os
from multiprocessing import Process, Manager

def f(dct, lst):
    dct[os.getpid()] = os.getpid()
    lst.append(os.getpid())
    print lst


if __name__ == '__main__':
    with Manager() as manager:
        dct = manager.dict()
        lst = manager.list(range(10))

        p_list = []

        for p in range(10):
            p = Process(target=f, args=(dct, lst))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print dct
        print lst



    
