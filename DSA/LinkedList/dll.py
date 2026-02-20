class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
if __name__=='__main__':
    head=node(10)
    
    second=node(20)
    
    third=node(30)
    head.next=second
    second.prev=third
    
    second.next=third
    third.prev=second
    
    temp=head
    while temp is not None:
        print(temp.data,end="")
        if temp.next is not None:
            print("<->",end="")
        temp=temp.next
    