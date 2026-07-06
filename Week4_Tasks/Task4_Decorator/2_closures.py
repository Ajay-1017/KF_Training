
# Closure - 1

# def outer_func(msg):
#     message  = msg

#     def inner_func():
#         print(message)

#     return inner_func

# hi_func = outer_func('Hi')
# hello_func = outer_func('Hello')

# hi_func()
# hello_func() 

# Closure - 2 using log

import logging
import os 

base_dir = os.path.dirname(__file__)

logging.basicConfig(
    level = logging.INFO,
    format = '%(name)s:%(levelname)s:%(message)s',
    filename = os.path.join(base_dir,'closure.log')
    )

def logger(my_func):
    def log_func(*args):
        logging.info('running {} with arguments {}'.format(my_func.__name__,args))
        print(my_func(*args))
    return log_func

def add(a,b):
    return a+b

def sub(a,b):
    return a-b


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(2,3)
sub_logger(5,4)






