class listnode:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list_type:
    def __init__(self):
        self.head = None
    def init_llt(self):
        self.head = None
    def addFirst(self, data):
        newNode = listnode(data)
        newNode.next = self.head
        self.head = newNode
    def add(self, pos, data):
        newNode = listnode(data)
        before = self.head
        for i in range(pos-1):
            before = before.next
        after = before.next
        before.next = newNode
        newNode.next = after

    def get(self, pos):
        before = self.head
        for i in range(pos):
            before = before.next
        return before.data
    def printlist(self):
        current = self.head
        while current :
            print(current.data, end="->")
            current = current.next
        print("NULL")
        print("=============")

list = linked_list_type()
for i in range(10):
    list.addFirst(i*10)
list.printlist()
list.add(6, -90)
list.printlist()
print(list.get(2))