# 1) Using module and get the function 

import my_module as m

lst = [1,2,3,4,5]
index = m.find_index(lst,4)
print(index)
print(m.test_var)


# 2) Directly access the function using 'from' keyword

# from my_module import find_index,test_var

# lst = [1,2,3,4,5]
# index = find_index(lst,4)
# print(index)
# print(test_var)

# 3) import sys -> to find list of python path file

# import sys
# import my_module
# print(sys.path)





