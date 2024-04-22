class Node:
    def __init__(self,item = None, Next = None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.item_count=0
    
    def isEmpty(self):
        return self.front == 0
    
    def Enqueue(self,data):
        new=Node(data)
        if self.isEmpty():             #when Empty
            self.front=new
        else:
            self.rear.next = new
        self.rear=new
        self.item_count+=1
    
    def Dequeue(self):
        if self.isEmpty():
            raise IndexError("empty queue")
        
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        
        else:
            self.front = self.front.next 
        self.item_count-=1
    
    def getFront(self):
        if self.isEmpty():
            raise IndexError("No data in queeue")
        else:
           return self.front.item
        
    def getRear(self):
        if self.isEmpty():
            raise IndexError("No data in queue ")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count

q1 = Queue()
q1.Enqueue(10)
q1.Enqueue(20)
q1.Enqueue(30)
print("front :",q1.getFront(),"Rear : ",q1.getRear())
print("size is ",q1.size())
