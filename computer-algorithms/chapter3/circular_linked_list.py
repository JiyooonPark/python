# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
def insert(list, data):
    newNode = Node(data, list.head)
    if (list.head):
        current = list.head
        while current.next and current.next is not list.head:
            current = current.next
        current.next = newNode
    else:
        list.head = newNode

# print method for the linked list
def printLL(list):
    current = list.head
    print(current.data)
    current = current.next
    while current and current is not list.head:
        print(current.data)
        current = current.next

# Singly Linked List with insertion and print methods
ll = LinkedList()
insert(ll, 3)
insert(ll, 4)
insert(ll, 5)
printLL(ll)