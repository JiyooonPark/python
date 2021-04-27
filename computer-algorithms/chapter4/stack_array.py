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


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
        stack.printStack()

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    stack.printStack()