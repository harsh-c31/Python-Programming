class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
def insertatend(head,x):
    newnode=Node(x)
    if head is None:
        return newnode
    last=head
    while last.next is not None:
        last=last.next
    last.next=newnode
    return head
def printlist(node):
    while node is not None:
        print(node.data,end="")
        if node.next is not None:
            print("->",end="")
        node=node.next
    print()
if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = insertatend(head, 6)

    printlist(head)