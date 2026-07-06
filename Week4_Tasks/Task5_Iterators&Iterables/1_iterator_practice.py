nums = [1,2,3] 
# List is an iterable (has __iter__()) but not an iterator
# because it does not implement __next__().


print(dir(nums)) # dir(obj) -> built in python function that shows you what attributes and methods an object as
# print(nums.__dir__()) # same as above python interally call this methods


# =======================================================================================================

# 1) converting the iterable into iterator

i_nums = iter(nums)
# i_nums = nums.__iter__()

# print(dir(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums)) # StopIteration 


# =======================================================================================================

# 2) To handle StopIteration Exception . It is done behind 'for loop'

# for loop hides all this 
# When you write

for num in nums:
    print(num)

# Python internally does something very similar to:

iterator = iter(nums)
while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:
        break


# =======================================================================================================
