class LinkedList:
    def __init__(self):
        self.length=0
        self.head=None
 

    def print_backward(self):
        print "[",
        if self.head != None:
            self.head.print_backward()
        print "]",
    
    def print_list(self):
        print "[",
        if self.head != None:
            self.head.print_list()
        print "]",
        
    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

class Node:
    
    def __init__(self, cargo=None, next=None):
        self.cargo=cargo
        self.next=next
    
    def __str__(self):
        return str(self.cargo)
        
    def print_list(self):
        while self:
            print self,
            self=self.next
        #print
     
    
    
    def print_backward(self):
        if self.next != None:
            tail = self.next
            tail.print_backward()
        print self.cargo,