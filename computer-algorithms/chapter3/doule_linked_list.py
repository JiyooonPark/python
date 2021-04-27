class DoubleNode:
    # constructor
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
class DoubleLinkedList:
    def __init__(self):
        self.head = None
def insert(list, data):
    if (list.head):
        current = list.head
        while (current.next):
            current = current.next
        newNode = DoubleNode(current,data)
        current.next = newNode
    else:
        newNode = DoubleNode(list.head, data)
        list.head = newNode
# print method for the linked list
def printLL(list):
    current = list.head
    while (current):
        print(current.data)
        current = current.next
def printLL_reverse(list):
    print("print reverse")
    current = list.head
    while (current.next):
        current = current.next
    while(current):
        print(current.data)
        current = current.prev

ll = DoubleLinkedList()
insert(ll, 3)
insert(ll, 4)
insert(ll, 5)
printLL(ll)
printLL_reverse(ll)