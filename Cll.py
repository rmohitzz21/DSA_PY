class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    
class Cll:
    def __init__(self,last=None):
        self.last= last
    
    def is_Empty(self):
        return self.last==None

    def insert_at_start(self,data):
        new=Node(data)
        if self.is_Empty():
            new.next=new
            self.last=new
        else:
            new.next=self.last.next
            self.last.next=new
    
    def insert_at_last(self,data):
        new=Node(data)
        if self.is_Empty():
            new.next-new
            self.last=new
        else:
            new.next=self.last.next
            self.last.next=new
            self.last=new

    def search(self,data):
        if self.is_Empty():
            return None
        temp=self.last.next               #1st node ref
        while temp!=self.last: #till the last node
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
                                                  

    def insert_after(self,temp,data):
        if temp is not None:
            new = Node(data,temp.next)     # after temp nodes reference temp.next
            temp.next=new
            if temp==self.last:
                self.last=new                    # if temp means data is last thn
        
    def print_list(self):
        temp= self.last.next                   # reference to first node
        while temp!= self.last:
            print(temp.item,end =' ')
            temp=temp.next
        print(temp.item)

    def delete_first(self):
        if not self.is_Empty():                          
            if self.last.next==self.last:                #if only 1 node is avl 
                self.last=None
            else:
                self.last.next=self.last.next.next    # reference to 2nd node
                                                    
    def delete_last(self):
        if not self.is_Empty():
            if self.last.next==self.last:                  #only if 1 node avl
                self.last=None
            else:
                temp=self.last.next                        # 1s node
                while temp.next != self.last:              #till the last second node 
                    temp=temp.next

    def delete_item(self,data):
        if not self.is_Empty():
            if self.last.next==self.last:                          #first is last
                  self.last=None
            else:
                if self.last.next.item==data:                          #first node to del
                    self.delete_first()
                else:
                    temp=self.last.next

                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                            break
                            if temp.next.item==data:
                                temp.next=temp.next.next
                                break
                            temp=temp.next
#     def __iter__(self):
#         if self.last==None:
#             return CllIterator(None)
#         else:
#             return CllIterator(self.last.next)

# class CllIterator:
#     def __init__(self,start):
#         self.current=start
#         self.start=start
#         self.count=0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current==None:
#             raise StopIteration
#             if self.current==self.current.next and self.count==1:
#                 raise StopIteration
#         else:
#             self.count=1
#             data=self.current.item
#             self.current=self.current.next
#             return data

mylist = Cll()
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_at_last(10)
mylist.insert_after(mylist.search(30),70)
mylist.insert_at_last(90)
# mylist.delete_item(70)
# mylist.delete_first()
# for x in mylist:
#     print(x ,end='')
mylist.print_list()

mylist.delete_item(90)
mylist.print_list()