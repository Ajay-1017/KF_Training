import logging 
import os

class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return self.first + " "+ self.last    

    @property
    def email(self):
        return self.first +"."+ self.last+"@gmail.com"
    
def main():
    base_dir = os.path.dirname(__file__)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

    file_handler = logging.FileHandler(os.path.join(base_dir,'demo_log','employee.log'))
    logger.addHandler(file_handler)
    file_handler.setFormatter(formatter)



    emp1 = Employee("ajay","balu")
    emp2 = Employee("akash","rajendran")

    logger.info(emp1.full_name)
    logger.info(emp2.email)

main()


