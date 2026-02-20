class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None    
def forward_traversal(head):
    curr=head
    while curr is not None:
        print(curr.data,end="")
        curr=curr.next
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