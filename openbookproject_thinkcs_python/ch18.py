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
        print
     
##### recursive inside the class not working!!!!! line 21     
        
    def print_backward(self):
        if self==None: return
        head=self
        tail=self.next
        print_backward(tail)
        print head,
        print