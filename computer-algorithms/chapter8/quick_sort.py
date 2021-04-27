def partition(arr, low, high):
    print("low:", str(low), "high:", str(high))
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr, "i+1 is", str(i+1))
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


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
arr = [10,9, 8, 7, 6, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
print(arr)