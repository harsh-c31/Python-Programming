class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def search(head,key):
    curr=head
    while curr is not None:
        if curr.data==key:
            return True
        curr=curr.next
    return False
if __name__=="__main__":
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
    head.next.next.next.next = node(5)
    key = 5
    if search(head, key):
        print("true")
    else:
        print("false")