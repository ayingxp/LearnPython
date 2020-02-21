# -*- coding: utf-8 -*-

u"""
事件驱动与异步IO:
    编写服务器处理程序时，有以下几种方式:
    1. 每收到一个请求，创建一个新的进程，来处理该请求(实现简单，进程开销大，性能较差)
    2. 每收到一个请求，创建一个新的线程，来处理该请求(涉及线程同步问题，可能会导致死锁问题)
    3. 每收到一个请求，放入一个事件列表，让主进程通过非阻塞I/O方式来处理请求(逻辑复杂)

示例-响应UI编程中的鼠标点击
    方式一：创建一个线程，该线程一直检测是否有鼠标点击
    缺点：CUP资源浪费; 如果扫描的设备多，则响应时间长；有可能阻塞

    方式二：事件驱动模型
    1. 有一个事件（消息）队列
    2. 鼠标按下时，往这个队列中增加一个点击事件（消息）
    3. 有个循环，不断从队列取出事件，根据不同的事件，调用不同的函数，如onClick(), onKeyDown()等
    4. 事件(消息)一般都各自保存各自的处理函数指针，这样，每个消息都有独立的处理函数；
"""

from multiprocessing import Process, Pool, Queue, Manager,
