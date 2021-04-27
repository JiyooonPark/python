from random import randint

def partition_mid(arr, middle):
    quickSort(arr, 0, len(arr)-1)
    print("Sorted", arr)
    key = find(arr, middle)
    print(key)
    return arr[:key], arr[key:key+count(arr, middle)+1], arr[key+count(arr, middle)+1:]

def partition(arr, low, high):
    # print("low:", str(low), "high:", str(high))
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            # print(arr)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # print(arr, "i+1 is", str(i+1))
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def find(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
def count(arr, key):
    c=0
    for i in arr:
        if i == key:
            c+=1
    return c
def findmatch(B, R):
    if len(B) ==0:
        return ()
    if len(B)==1:
        return (B[0], R[0])
    b = B[0]
    print("key is :", str(b))
    Rlt, Req, Rgt = partition_mid(B, b)
    print(Rlt, Req, Rgt)
    r = Req[1]



if __name__=="__main__":
    b = [randint(1,100) for i in range(4)]
    r = [randint(1,100) for i in range(4)]
    print("b : ", b)
    print("r: ", r)
    findmatch(b,r)
