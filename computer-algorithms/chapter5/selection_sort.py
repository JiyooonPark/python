
def swap(a, b):
    return b, a
def selection_sort(L):
    for i in range(len(L)):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = swap(L[i], L[min_index])
L = [3, 1, 41, 59, 26, 53, 5]
print(L)
selection_sort(L)

# Let's see the list after we run the Selection Sort
print(L)