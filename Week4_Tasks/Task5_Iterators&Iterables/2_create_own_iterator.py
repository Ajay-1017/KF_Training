
# 1) Creating iterators using own class
class MyRange:

    def __init__(self,start,end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
        current = self.value
        self.value+=1
        return current


# Creating iterators using generator

def gen_range(start,end):
    current = start
    while start < end:
        yield current
        current+=1

cls_nums = MyRange(1,10)

gen_nums= gen_range(1,10)


# print(next(cls_nums))
# print(next(cls_nums))
# print(next(cls_nums))
# print(next(cls_nums))
# print(next(cls_nums))
# for num in cls_nums:
#     print(num)

print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))

for num in gen_nums:
    print(num)
