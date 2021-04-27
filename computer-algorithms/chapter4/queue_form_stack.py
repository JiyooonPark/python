max_size = 15
class Stack:
    def __init__(self):
        self.stack = [None for i in range(max_size)]
        self.size = 0
    def printStack(self):
        for i in self.stack:
            print(i, end="|")
        print()
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.stack[self.size-1]

    def push(self, value):
        self.stack[self.size] = value
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.stack[self.size-1]
        self.stack[self.size-1] = None
        self.size -= 1
        return remove
class queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def dequeue(self):
        for i in range(self.stack1.size):
            self.stack2.push(self.stack1.pop())
        key = self.stack2.pop()
        for i in range(self.stack2.size):
            self.stack1.push(self.stack2.pop())
        return key
    def enqueue(self, val):
        self.stack1.push(val)
    def printQueue(self):
        print("Stack 1: ", end=" ")
        for i in self.stack1.stack:
            print(i, end="|")
        print("\nStack 2: ", end=" ")
        for i in self.stack2.stack:
            print(i, end="|")
        print()

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.printQueue()
print(q.dequeue())
q.printQueue()
