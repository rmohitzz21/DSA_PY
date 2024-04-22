class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Deque:
    def __init__(self):
        self.front=None
        self.Rear=None
        self.item_count=0
    
    def is_Empty(self):
        return self.item_count == 0
    
    def insert_Front(self,data):
        new =Node(None,data,self.front)
        if self.is_Empty():
            self.front=new
            self.Rear=new
        else:
            self.front.prev=new
            self.front=new
        self.item_count += 1

    def insert_Rear(self,data):
        new = Node(self.Rear,data,None)
        if self.is_Empty():
            self.front=new
            self.Rear=new
        else:
            self.Rear.next=new
            self.Rear=new
        self.item_count += 1
    
    def delete_front(self): 
        if self.is_Empty():
            raise IndexError("Deque is Empty")
        
        if self.front == self.Rear:
            self.front=None
            self.Rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count -= 1

    def delete_Rear(self):
        if self.is_Empty():
            raise IndexError("Deque is empty")

        if self.front==self.Rear:
            self.front=None
            self.Rear=None

        else:
            self.Rear.prev=self.Rear
            self.Rear.next=None
        self.item_count -= 1
    
    def get_front(self):
        if self.is_Empty():
            raise IndexError("Deque is Empty")
        else:
            return self.front.item

    def get_Rear(self):
        if self.is_Empty(self):
            raise IndexError("Deque is empty")
        else:
            return self.Rear.item
    
    def size(self):
        return self.item_count

d1 =Deque
d1.insert_Front(10)
d1.insert_Front(20)
d1.insert_Rear(30)
d1.insert_Rear(40)
print("Size is :", d1.size())