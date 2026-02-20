class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def delnode(head,pos):
    temp=head
    if pos==1:
        head=head.next
        return head
    prev=None
    for i in range(1,pos):
        prev=temp
        temp=temp.next
    prev.next=temp.next
    return head
def printlist(head):
    while head is not None:
        print(f"{head.data}->",end="")
        head=head.next
    print("null pointer")