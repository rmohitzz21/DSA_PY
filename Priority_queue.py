# PRIORITY QUEUE IMPLEMENTATION USING LIST CONCEPT

# 1. DEFINE A CLASS PRIORITYQUEUE TO IMPLEMET PRIORITY QUEUE DATA STRUCTURE USING LIST . 
# PROVE __INIT__() METHOD TO CREATE LIST OBJECT.

#2. DEFINE PUSH METHOD TO INSERT NEW DATA WITH GIVEN PRIORITY

#3. DEFINE POP METHOD WHICH RETURN THE HIGHEST PRIORITY STORED PRIORITY DATA STRUCTURE. 
# RAISE EXCEPTION IF PRIORITY QUEUE IS EMPTY.

#4.DEFINE IS_EMPTY METHOD

#5.DEFINE SIZE METHOD

class PriorityQueue:
    def __init__(self):
        self.items=[]

    def is_Empty(self):
        return len(self.items)==0
    
    def push(self,data,priority):
        index =0 
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))

    def pop(self):
        if self.is_Empty():
            raise IndexError("priority queue is empty")
        return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)
    
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