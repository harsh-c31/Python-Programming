class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
def insertatfront(head,x):
    newNdoe=Node(x)
    newNdoe.next=head
    return newNdoe
def printlist(head):
    curr=head
    while curr is not None:
        print(curr.data,end="")
        if curr.next is not None:
            print("->",end="")
        curr=curr.next
    print()
if __name__=="__main__":
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    # Insert a new node at
    # the front of the list
    x = 1
    head = insertatfront(head, x)

    # Print the updated list
    printlist(head)