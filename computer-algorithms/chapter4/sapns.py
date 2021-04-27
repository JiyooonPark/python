from random import randint
def spans(arr):
    ans = [None for i in range(len(arr))]
    for i in range(len(arr)):
        print(arr[i])
        count = 0
        for j in range(i,-1,-1):
            print(i, j)
            if arr[j] > arr[i]:
                break
            else:
                # print(arr[j], arr[i])
                count +=1
        ans[i] = count
    print(ans)

if __name__=="__main__":
    arr = [randint(1,100) for i in range(4)]
    arr = [60, 30, 40, 20, 50, 30]
    print(arr)
    spans(arr)