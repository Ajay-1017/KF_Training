import logging
import employee
import os


base_dir = os.path.dirname(__file__)

os.makedirs(os.path.join(base_dir,'demo_log'),exist_ok=True)

logging.basicConfig(
    filename = os.path.join(base_dir,'demo_log','cal.log'),
    level=logging.DEBUG,
    format ='%(name)s:%(levelname)s:%(message)s'
    )


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def main():
    a=2
    b=1
    add_res = add(a,b)
    sub_res = sub(a,b)

    logging.info(f"addition -> {add_res}")
    logging.info(f"sub -> {sub_res}")

main()


























