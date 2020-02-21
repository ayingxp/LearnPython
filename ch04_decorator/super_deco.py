# -*- coding: utf-8 -*-

import time

user = 'jiwaaying'
passwd = '123456'

def auth(func):
    def wrapper(*args, **kwargs):
        username = raw_input('Username:').strip()
        password = raw_input('Password:').strip()

        if user == username and passwd == password:
            print '\033[32;1mUser has passed authentication\033[0m'
            res = func(*args, **kwargs)
            print '---after authentication'
            return res
        else:
            exit('\033[32;1mInvalid username or password\033[0m')

    return wrapper

@auth
def index():
    print 'Welcome to index page'

@auth
def home():
    print 'Welcome to home page'
    return 'from home'

#auth
def bbs():
    print 'Welcome to bbs page'


#index()
res = home() # 实际调用的是wrapper函数
print 'res is: ', res
#bbs()


