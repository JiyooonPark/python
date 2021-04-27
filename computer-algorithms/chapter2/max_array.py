# find max element in array
def max_of_array(arr, n):
    max = arr[0]
    for i in range(n):
        if max<arr[i]:
            max = arr[i]
    return max

def min_max(arr, n, min, max):
    if n == 0:
        return [min, max]
    else:
        if arr[n] < min:
            min = arr[n]
        if arr[n] > max:
            max = arr[n]
        return min_max(arr, n-1, min, max)

def my_max(x, y):
    if x> y:
        return x
    else:
        return y

def my_min(x, y):
    if x> y:
        return y
    else:
        return x
arr = [10,2,23,12,22,14,552,432,3,334,4436]
print( "max of array is", str(max_of_array(arr, len(arr))))