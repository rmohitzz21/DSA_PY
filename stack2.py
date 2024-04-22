# stack extending list

# create class to implement stack data structure by extending List class
# define is_empty() method to check if stack is empty
# define Push()
# define Pop()
class stack(list):
    def is_Empty(self):
        return len(self)==0
    
    def Push(self,data):
        self.append(data)
    
    def pop(self):
        if not self.is_Empty():
            super().pop()
        else:
            raise IndexError("Stack is Empty")
    def Peek(self):
        if not self.is_Empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No Attribute insert in stack")

s1 = stack()
s1.Push(10)
s1.Push(20)
s1.Push(30)
print(s1.size())
print(s1.Peek())
print(s1.pop())
print(s1.size())



