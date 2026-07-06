
from functools import wraps
# 1 - Use case (logging)

def my_logger(func):
    import os
    import logging

    base_dir = os.path.dirname(__file__)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(os.path.join(base_dir,f'{func.__name__}.log'))
    logger.addHandler(file_handler)

    formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
    file_handler.setFormatter(formatter)

    streamer = logging.StreamHandler()
    logger.addHandler(streamer)
    streamer.setFormatter(formatter)
    streamer.setLevel(logging.INFO)



# @wraps(func)
# Copies the original function's information (__name__, __doc__, etc.)
# to the wrapper function.
#
# Without @wraps:
#     add.__name__ -> wrapper
#
# With @wraps:
#     add.__name__ -> add
#
# Simple memory:
# "The wrapper behaves like the original function."

    @wraps(func)
    def wrapper_func(*args,**kwargs):
        logger.debug('function {} with arguments {} and keyword arguments {}'.format(func.__name__,args,kwargs))
        logger.info('function {} with arguments {} and keyword arguments {}'.format(func.__name__,args,kwargs))
        return func(*args)

    return wrapper_func

# @my_logger
# def add(a,b):
#     return a+b
# print(add(1,2))


# 2 - Use case (timing) 

def my_timer(func):
    import time

    @wraps(func)
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        run_time = t2 - t1
        print("start_time :",t1)
        print(f"total run time of {func.__name__} is {run_time} sec")
        print("end_time :",t1)
        return result
    return wrapper

# import time
# @my_timer
# def add(a,b):
#     time.sleep(1)
#     return a+b
# print("addtion :",add(1,2))


# stacking multiple decorators for the single function
# @A @B is simply A(B(function))
import time


@my_logger
@my_timer
def add(a,b):
    time.sleep(1)
    return a+b
print("addtion :",add(1,2))

# add = my_timer(add)
# print(add.__name__)  


# @my_timer
# @my_logger
# def add(a,b):
#     time.sleep(1)
#     return a+b
# print("addtion :",add(1,2))
