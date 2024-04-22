
from SLL import *
class Stack(SLL):
    def __init__(self):
        super().__init__()             # Access parent class init method which contain start 
        self.itemCount=0
    
    def is_Empty(self):
        return super().is_Empty()
    
    def Push(self,data):
        self.insert_at_start(data)
        self.itemCount+=1
    
    def pop(self):
      if not self.is_Empty():
        self.delete_first()
        self.itemcount-=1
      else:
        raise IndexErrror("Stack is Empty ")
    
    def Peek(self):
        if not self.is_Empty():
            return self.start.item
    
    def size(self):
        if not self.is_Empty():
            return self.itemCount
s1=Stack()
s1.Push(10)
s1.Push(20)
s1.Push(30)
print("\nThe size of Stack ",s1.size())
        