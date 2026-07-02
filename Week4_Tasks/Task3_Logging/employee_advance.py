import logging
import os

base_dir = os.path.dirname(__file__)
# __file__ gives the path of the current file.
# os.path.dirname() returns the directory containing that file.

logger = logging.getLogger(__name__) 
# If this file is run directly, __name__ is "__main__",
# so the logger name becomes "__main__".
# If this file is imported, __name__ is the module name,
# so the logger name becomes the module's name.

logger.setLevel(logging.INFO) # Set the minimum logging level for this logger.

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s') # Define how each log message should be formatted.

file_handler = logging.FileHandler(os.path.join(base_dir,'log','employee.log')) # Create a FileHandler that writes log messages to employee.log.

logger.addHandler(file_handler) # Attach the FileHandler to the logger so log messages are written to the file.

file_handler.setFormatter(formatter) # Apply the formatter so log messages are written in the specified format.

file_handler.setLevel(logging.ERROR)


class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        
        logger.info(f"created employee : ({self.full_name} , {self.email}) ")

    @property
    def full_name(self):
        return self.first + self.last
    
    @property
    def email(self):
        return self.first +"."+self.last+"@gmail.com"

emp1 = Employee("Ajay","Balu")
emp2 = Employee("Aravinth", "Seelan")
