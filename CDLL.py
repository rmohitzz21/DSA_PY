class Node:
    def __init__(self , item=None,prev=None, next=None):
        
        self.item=item
        self.prev=prev
        self.next=next

class Cdll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        new=Node(data)
        if self.is_empty():
            new.next=new                #only if list is empty first node inserted which ref itself
            new.prev=new
        else:
            new.next=self.start               
            new.prev=self.start.prev
            
            self.start.prev.next=new                   #last node next --> new node
            self.start.prev=new                        #first node prev --> new node

        self.start=new                                 #start --> new
    
    def insert_at_last(self,data):
        new =Node(data)
        if self.is_empty():       #only if list is empty first node inserted which ref itself
            new.next=new
            new.prev=prev
            self.start=new
        else:
            new.next = self.start
            new.prev = self.start.prev 

            new.prev.next=new          # last 2nd node next  ->new node
            self.start.prev=new        # first node prev --> new node

    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next

        while temp!=self.start:
            if temp.item==data:
                return temp
            temp=temp.next
        return None

    def insert_after(self,temp,data):
        if temp is not None:
            new=Node(data)

            new.next=temp.next        #--|
            new.prev=temp             #--  new node data 

            temp.next.prev=new        #add new node in the list 
            temp.next=new          

    def delete_first(self):
        if self.start is not None:
            if self.start.next==self.start:               # only 1 node avl in list
                self.start=None
            else:
                self.start.prev.next=self.start.next         # last node  next ref --> to starting 2nd node then 1st node is skip
                self.start.next.prev=self.start.prev           # 2nd node prev ref --> last node
                self.start=self.start.next                    # start ref--> 2nd node

    def delete_last(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start                 # 2nd last node next ref--> first node
                self.start.prev=self.start.prev.prev                 # 1st node prev ref -->  2nd last node

    def delete_item(self,data):
        if self.start is not None:
            temp=self.start                           # first node temp
            if temp.item==data:                        
                self.delete_first()
            else:
                temp=temp.next   
                while temp is not self.start:
                    if temp.item==data:
                        temp.next.prev=temp.prev            #temp nexts node prev ref -> temp prev node
                        temp.prev.next=temp.next             #temp prev nodes next ref -> temo next node
                    temp=temp.next
    
    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
            while temp is not self.start:
                print(temp.item,end=' ')
                temp=temp.next
    
    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration

        if self.current==self.start and self.count==1:
            raise StopIteration
        
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data



mylist = Cdll()
# mylist.insert_at_last(10)
mylist.insert_at_start(2)
mylist.insert_after(mylist.search(2),10)
mylist.insert_at_last(30)
# mylist.insert_after(mylist.search(10),10)
# mylist.print_list()
# mylist.delete_first()
# mylist.delete_last()
mylist.delete_item(10)
for x in mylist:
    print(x ,end=' ')