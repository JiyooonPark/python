def arraymax(arr):
    if len(arr) is 1:
        return arr[0]
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        print(arr)
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        print(lefthalf, righthalf)

        left = arraymax(lefthalf)
        right = arraymax(righthalf)
        if left > right:
            print("left is bigger:", str(left))
            return left
        else:
            print("right is bigger:", str(right))
            return right


nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70,32,2,1,2,32,1321,2,2321,1]
max = arraymax(nlist)
print(max)
