class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class stack:
    def __init__(self):
        self.start=None
        self.itemCount=0
    
    def is_Empty(self):
        return self.start==None
    
    def Push(self,data):
        new=Node(data,self.start)
        self.start=new                       #First node
        self.itemCount+=1
    
    def pop(self):
        if not self.is_Empty():
            data=self.start.item
            self.start=self.start.next
            self.itemCount-=1
            return self.start
        else:
            raise IndexErrror("Stack is empty")

    def Peek(self):
        if not self.is_Empty():
            return self.start.item
        else:
            raise self.is_Empty()

    def size(self):
        return self.itemCount
    
s1 =stack()
s1.Push(10)
s1.Push(20)
s1.Push(30)
print("The size of stack is ",s1.size())
print("top Elment of stack is ", s1.Peek())
s1.pop()
print("The size of stack is",s1.size())
print()