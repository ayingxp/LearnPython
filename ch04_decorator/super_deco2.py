# -*- coding: utf-8 -*-

import time

user = 'jiwaaying'
passwd = '123456'

def auth(auth_type):
    def outer_wrapper(func):
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
    return outer_wrapper


@auth
def index():
    print 'Welcome to index page'

@auth(auth_type='local')
def home():
    print 'Welcome to home page'
    return 'from home'

#auth(auth_type='remote')
def bbs():
    print 'Welcome to bbs page'


#index()
res = home() # 实际调用的是wrapper函数
print 'res is: ', res
#bbs()


