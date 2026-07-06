

# 1) using list
def square1(nums):
    res=[]
    for i in nums:
        res.append(i*i)
    return res

print(square1([1,2,3,4,5,6])) 

# 2) list comprehension 
my_res = [x*x for x in [1,2,3,4,5,6] ]
print(my_res)


# 3) using generators

def square2(nums):
    for i in nums:
        yield i*i

my_nums = square2([1,2,3,4,5,6])

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

for i in my_nums:
    print(i)

# 4) generator expression
my_res = (x*x for x in [1,2,3,4,5,6])

print(my_res)

for i in my_res:
    print(i)


# 5) Peformance caluculation between generators and list
import random
import time
from memory_profiler import memory_usage

names = ['ajay','aravinth','kishore','balaji','arjun','harish']
major = ['cs','it','bcom','ece','aids','biotech']

def people_list(num_people):
    res=[]
    for i in range(num_people):
        res.append(
            {
                "id":i,
                "name":random.choice(names),
                "major": random.choice(major)
            }
        )
    return res
    

def people_genarator(num_people):
    for i in range(num_people):
        res = {
                "id":i,
                "name":random.choice(names),
                "major": random.choice(major)
            }
    yield res

print("memory usage before {}mb".format(memory_usage()[0]))

# t1 = time.time()
# lst = people_list(1000000)
# t2 = time.time()


t1 = time.time()
lst = people_genarator(1000000)
t2 = time.time()

print("memory usage before {}mb".format(memory_usage()[0]))
print("took seconds {}".format(t2-t1))

