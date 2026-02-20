class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#implementation
node1=Node(15)
node2=Node(23)
node3=Node(54)
node4=Node(64)

node1.next=node2
node2.next=node3
node3.next=node4
head=node1 #point head towards node1
current=head #make head as current
while current:
    print(current.data,end="->")
    current=current.next
print("Null")