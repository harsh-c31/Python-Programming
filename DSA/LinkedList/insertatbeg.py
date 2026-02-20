class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None    
def insertatfront(head,new_data):
    new_node=Node(new_data)
    new_data.next=head
    if head is not None:
        head.prev=new_node
    return new_node
def printlist(head):
    curr=head
    while curr is not None:
        print(curr.data,end="")
        if curr.next is not None:
            print("<->",end="")
        curr=curr
    print()
if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal: ", end="")
    forward_traversal(head)