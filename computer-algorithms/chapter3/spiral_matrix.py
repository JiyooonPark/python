def spiral(arr, n, m):
    left = 0
    right = m-1
    top = 0
    bottom = n-1
    val = 1
    while left<=right and top<=bottom:
        # print(val)
        for i in range(left, right+1):
            arr[top][i] = val
            val+=1
            # print(arr)
        top+=1
        for i in range(top, bottom+1):
            # print(i, right)
            arr[i][right] = val
            val+=1
            # print(arr)
        right-=1
        print(val)
        for i in range(right, left-1, -1):
            arr[bottom][i] = val
            val += 1
            # print(arr)
        bottom-=1
        for i in range(bottom, top-1, -1):
            arr[i][left] = val
            val+=1
        left +=1
    return arr

list=[[0 for i in range(5)] for j in range(4)]
list = spiral(list, 4, 5)
for a in list:
    print(a)