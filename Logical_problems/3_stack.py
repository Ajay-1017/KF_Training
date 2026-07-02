
class Stack:
    def __init__(self,lst):
        self.lst = lst
    
    def push(self,value):
        self.lst.append(value)
        return self.lst

    def peek(self):
        if self.lst == []:
            return "your list is empty"
        else:
            return self.lst[-1]
    
    def pop(self):
        if self.lst == []:
            return "your list is empty"
        else:
            self.lst.pop()
            return self.lst
    
    def is_empty(self):
        if self.lst == []:
            return True
        else:
            return False
    

s = Stack([1,2,3,4,5,6,7,8,9])
print(s.push(10))
print(s.push(20))
print(s.peek()) 
print(s.pop()) 
print(s.is_empty())


    

