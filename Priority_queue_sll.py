class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self):
        self.start=None
        self.itemCount=0
    
    def push(self,data,priority):
        new = Node(data,priority)
        if not self.start  or priority < self.start.priority:
            new.next=self.start   # new node ref-> first node
            self.start=new
        else:
            temp=self.start
            while temp.next != None and temp.priority <= priority:
                temp=temp.next
            new.next=temp.next
            temp.next=new
        self.itemCount+=1
    
    def is_Empty(self):
        return self.start==None
    
    def pop(self):
        if self.is_Empty():
            raise IndexError("Queue is Empty")

        data=self.start.item
        self.start=self.start.next
        self.itemCount-=1
        return data
        self.itemCount-=1

    def size(self):
        return self.itemCount

p = PriorityQueue()
p.push("Amit",4)
p.push("Max",1)
p.push("Ananat",7)
p.push("Agrah",2)
p.push("Ashima",5)
p.push("Arjun",8)

print(p.size())

while not p.is_Empty():
    print(p.pop())
