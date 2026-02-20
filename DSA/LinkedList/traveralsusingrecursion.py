class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traversal(head):
    if head is None:
        print()
        return
    print(head.data,end="")
    
    if head.next is not None:
        print("->",end="")
    traversal(head.next)

if __name__ == "__main__":

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traversal(head)