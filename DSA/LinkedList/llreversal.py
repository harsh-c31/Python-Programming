class node:
    def __init__(self,data):
        self.data=data
        self.next=None


def reversal(head):
    curr=head
    prev=None
    while curr is not None:
        nextnode=curr.next #store next
        curr.next=prev#reverse curr nodes next pointer to prev
        #move one pointer ahead
        prev=curr
        curr=nextnode
    return prev
def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()


if __name__ == "__main__":

    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
    head.next.next.next.next = node(5)
    head = reversal(head)
    printList(head)