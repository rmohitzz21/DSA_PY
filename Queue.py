class Queue:
    def __init__(self):
        self.items =[]
        self.front=None
        self.rear=None
    
    def is_empty(self):
        return len(self.items)==0
    
    def Enqueue(self,data):
        self.items.append(data)
    
    def Dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue UnderFlow")
    
    def getFront(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
    
    def getRear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")
    
    def size(self):
        return len(self.items)

q1= Queue()
q1.Enqueue(10)
q1.Enqueue(20)
q1.Enqueue(30)
# print("size is ",q1.size())
# print("get front",q1.getFront())
# print("get Rear",q1.getRear())
# q1.Dequeue()
# print("size is ",q1.size())
try:
    print(q1.getFront())
except IndexError as e:
    print(e.args[0])

print("front = ",q1.getFront(),"Rear=",q1.getRear())
