class QueueNode:
    def __init__(self, data):
        self.data = data
        self.link = None
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def initQueue(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        temp = QueueNode(data)
        if self.is_empty():
            self.front = temp
            self.rear = temp
        else:
            self.rear.link = temp
            self.rear = temp
    def printQueue(self):
        curr = self.front
        while curr:
            print(curr.data, end="-> ")
            curr = curr.link
        print("\n=================")
    def dequeue(self):
        if self.is_empty():
            return "is empty"
        else:
            data = self.front.data
            self.front = self.front.link
            print("returning :", str(data))
            return data

q = LinkedQueue()
for i in range(10):
    q.enqueue( i)
q.printQueue()
q.dequeue()

q.printQueue()

