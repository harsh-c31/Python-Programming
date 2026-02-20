class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removelast(head):
    # empty list
    if head is None:
        return None

    # only one node
    if head.next is None:
        return None

    # find second last node
    secondlast = head
    while secondlast.next.next is not None:
        secondlast = secondlast.next

    # remove last node
    secondlast.next = None
    return head

def printlist(head):
    while head is not None:
        print(head.data, end="")
        if head.next:
            print("->", end="")
        head = head.next
    print("->None")

if __name__ == "__main__":
    head = node(8)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(1)
    head.next.next.next.next = node(7)

    head = removelast(head)
    printlist(head)
