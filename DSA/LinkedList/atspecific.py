class node:
    def __init__(self, x):
        self.data = x
        self.next = None

def insertatpos(head, pos, val):
    if pos < 1:
        return head

    # insert at beginning
    if pos == 1:
        newNode = node(val)
        newNode.next = head
        return newNode

    curr = head
    for i in range(1, pos - 1):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head

    newNode = node(val)
    newNode.next = curr.next
    curr.next = newNode
    return head

def printlist(head):
    curr = head
    while curr:
        print(curr.data, end="")
        if curr.next:
            print("->", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
    head.next.next.next.next = node(5)

    printlist(head)

    val, pos = 3, 3
    head = insertatpos(head, pos, val)
    printlist(head)




