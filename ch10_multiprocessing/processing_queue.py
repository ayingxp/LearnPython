# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'Hello'])


def f2():
    print 'In f2 func ...'
    q.put([42, None, 'Hello'])


if __name__ == '__main__':
    #import Queue
    #q = Queue.Queue()
    q = Queue()
    p = Process(target=f2, )
    p.start()
    print q.get()
    p.join()
    print 'done ...'
