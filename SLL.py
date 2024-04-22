#DEFINE CLASS NODE TO DES NODE IN SLL 

class Node:
    def __init__(self,item=None, next=None):
        self.item = item
        self.next = next


# DEFINE CLASS SLL TO IMPLEMENT SLL WITH __INIT__() METHOD TO CREATE AND INITIALISE START REFERNCE VARIABLE VARIABLE .

class SLL:
    def __init__(self,start = None):
        self.start =start
    

# DEFINE METHOD IS_EMPTY() TO CHECK LIST IS EMPTY 

    def is_Empty(self):
        return self.start==None

# METHOD INSERT_AT_START TO INSERT ELEMENT 

    def insert_at_start(self,data):
        n=Node(data,self.start)                                            
        self.start=n                                                            

# METHOD INSERT_AT _LAST TO INSERT ELEMENT 

    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_Empty():
            temp=self.start
            while temp.next is not  None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n

    def insert_after(self,temp,data):
        if temp is not None:              
            n=Node(data,temp.next)
            temp.next=n
    
#  METHOD SEARCH 

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp = temp.next
        return None


# Method Print
 
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp=temp.next
        
# delete First Element
 
    def delete_first(self):
        if self.is_Empty():
            print("List is Empty")
        elif self.start is not None:
            self.start= self.start.next
        else:
            self.start=None
        
    
# delete Last Element 

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None                    #only one node
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

# delete any item in list

    def delete_item(self,data):
        if self.start is not None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next = temp.next.next



my_list = SLL()
my_list.insert_at_start(1)
my_list.delete_first()
# my_list.insert_at_last(20)
# my_list.insert_after(my_list.search(20),25)
# my_list.insert_at_last(30)
# my_list.insert_at_last(40)
my_list.print_list()

# my_list.delete_last()

