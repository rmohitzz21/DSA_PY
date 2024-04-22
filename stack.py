class Stack:
    def __init__(self):
        self.item=[]
    
    def is_Empty(self):
        return len(self.item)==0
    
    def Push(self,data):
        self.item.append(data)
    
    def Pop(self):
        if not self.is_Empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is Empty")
        
    def Peek(self):
        if not self.is_Empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return len(self.item)

s1=Stack()
s1.Push(10)
s1.Push(20)
s1.Push(30)
print(s1.Peek())
print(s1.size())
print(s1.Pop())