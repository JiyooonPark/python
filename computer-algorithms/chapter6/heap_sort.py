max_size = 20
class HeapType:
    def __init__(self):
        self.heap = [None for i in range(max_size)]
        self.heapsize = 0
    def init_heap(self):
        self.heapsize = 0
    def upHeap(self):
        i=self.heapsize
        key = self.heap[self.heapsize]
        while (i!=1) and (key<self.heap[i//2]):
            self.heap[i] = self.heap[self.heapsize//2]
            i //=2
        self.heap[i] = key
    def printHeap(self):
        for i in range(1, self.heapsize+1):
            print(self.heap[i], end=" ")
        print()
    def insertItem(self, key):
        self.heapsize +=1
        self.heap[self.heapsize]=key
        self.upHeap()
        self.printHeap()
    def downHeap(self):
        temp = self.heap[1]
        parent = 1
        child = 2
        while child <= self.heapsize:
            if child<self.heapsize and self.heap[child]>self.heap[child+1]:
                #find the smaller child
                child +=1
            if temp <= self.heap[child]:
                # if smaller than the smaller child, break
                break
            # if the child is smaller than root,
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2
        self.heap[parent] = temp
    def removeMin(self):
        key = self.heap[1]
        self.heap[1] = self.heap[self.heapsize]
        self.heapsize -=1
        heap = self.downHeap()
        return key
    def heapsort(self, list):
        for i in range(0, self.heapsize):
            list[i] = self.removeMin()
    def inPlaceHeapSort(self):
        size = self.heapsize
        key = 0
        for i in range(size):
            key = self.removeMin()
            heap.heap[heap.heapsize+1] = key


heap = HeapType()
heap.init_heap()
heap.insertItem( 5)
heap.insertItem( 125)
heap.insertItem(53)
heap.insertItem(15)
heap.insertItem( 225)
heap.insertItem(55)
list = [None for i in range(max_size)]
heap.heapsort( list)
print(list)
