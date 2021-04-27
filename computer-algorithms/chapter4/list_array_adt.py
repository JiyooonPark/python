max_size = 15
class arraylist:
    def __init__(self):
        self.list=[i for i in range(max_size)]
        self.size = 0
    def init_list(self):
        self.size = 0

    def traverse(self):
        for i in range(self.size):
            print(self.list[i], end=" ")
        print("\n==================")
    def add(self, pos, data):
        if self.size == max_size:
            print("array is full")
            exit(1)
        for i in range(self.size, pos-1, -1):
            self.list[i+1] = self.list[i]
        self.list[pos] = data
        self.size = self.size+1
    def remove(self, pos):
        item = self.list[pos]
        for i in range(pos+1, self.size):
            self.list[i-1] = self.list[i]
        self.size = self.size-1
        return item

ar = arraylist()
ar.traverse()
ar.add( 0, 100)
ar.add(0, 200)
ar.add( 0, 300)
ar.add(0, 400)
ar.add(0, 500)
ar.add( 3, 1500)


ar.traverse()
# print(len(ar.list))
print(ar.remove( 3))
ar.traverse()