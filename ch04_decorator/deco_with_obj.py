# -*- coding: utf-8 -*-

from functools import wraps

import time

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + ' with obj was called!'
            print log_string
            
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')

            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        print 'send a notify message!'

class email_logit(logit):
   def __init__(self, email='hello@qq.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

   def notify(self):
        pass


@logit()
def myfunc_with_obj():
    pass


myfunc_with_obj()
