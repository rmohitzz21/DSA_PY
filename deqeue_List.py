class Dequeue:
    def __init__(self):
        self.items=[]
    
    def is_Empty(self):
        return len(self.items)==0
    
    def insert_Front(self,data):
        self.items.insert(0,data)
    
    def insert_Rear(self,data):
        self.items.append(data)
    
    def delete_front(self):
        if self.is_Empty():
            raise IndexError("Dequeue is Empty")
        
        else:
            self.items.pop(0)
    
    def delete_Rear(self):
        if self.is_Empty():
            raise IndexError("Dequeue is Empty")
        else:
            self.items.pop()
    
    def get_Front(self):
        if self.is_Empty():
            raise IndexError("Dequeue is Empty")
        else:
            return self.items[0]
    
    def get_Rear(self):
        if self.is_Empty():
            raise IndexError("Dequeue Is Empty")
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
d1 = Dequeue()
d1.insert_Front(10)
d1.insert_Front(20)
d1.insert_Rear(30)
d1.insert_Rear(40)

print("Size is ",d1.size())
print("Front :", d1.get_Front()," Rear :", d1.get_Rear())
