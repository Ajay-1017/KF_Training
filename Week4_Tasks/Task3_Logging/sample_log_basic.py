import logging
import employee_advance
import os

Base_dir = os.path.dirname(__file__)

os.makedirs(os.path.join(Base_dir,'log'),exist_ok=True)

logging.basicConfig(
    filename = os.path.join(Base_dir,'log','test.log'),
    level = logging.DEBUG , 
    format = '%(asctime)s : %(levelname)s : %(message)s'
    ) # After changing the basic config (debug and below) also shown in console


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main():
    a = 6
    b = 3

    add_res = add(a,b)
    logging.debug(f"add : {a} + {b} = {add_res}") # # debug will not shown in console we need to change the basic_config

    sub_res = sub(a,b)
    logging.debug(f"sub : {a} - {b} = {sub_res}") # nfo will not shown in console we need to change the basic_config

    mul_res = mul(a,b)
    logging.info(f"mul : {a} * {b} = {mul_res}") # default

    div_res = div(a,b)
    logging.critical(f"div : {a} / {b} = {div_res}") # default
    
main()

