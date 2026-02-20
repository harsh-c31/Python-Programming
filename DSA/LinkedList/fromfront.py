class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
def delhead(head):
    if head is None:
        return None
    temp=head
    head=head.next
    temp=None
    return head

def printlist(curr):
    while curr is not None:
        print(curr.data,end="")
        if curr.next is not None:
            print("->",end="")
        curr=curr.next
        
if __name__=='__main__':
    head = Node(8)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(7)

    head = delhead(head)  
    printlist(head)