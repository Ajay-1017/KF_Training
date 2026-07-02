import logging
import employee_advance
import os

Base_dir = os.path.dirname(__file__)

os.makedirs(os.path.join(Base_dir,'log'),exist_ok=True)

base_dir = os.path.dirname(__file__)

logger = logging.getLogger(__name__) 


logger.setLevel(logging.INFO) 

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(os.path.join(base_dir,'log','cal_advance.log')) 

logger.addHandler(file_handler)

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try :
        res = a/b
    except ZeroDivisionError:
        return logger.error("try to divide by zero")
    else:
        return res

def main():
    a = 6
    b = 0

    add_res = add(a,b)
    logger.debug(f"add : {a} + {b} = {add_res}") # # debug will not shown in console we need to change the basic_config

    sub_res = sub(a,b)
    logger.debug(f"sub : {a} - {b} = {sub_res}") # nfo will not shown in console we need to change the basic_config

    mul_res = mul(a,b)
    logger.info(f"mul : {a} * {b} = {mul_res}") # default

    div_res = div(a,b)
    logger.info(f"div : {a} / {b} = {div_res}") # default
    
main()

