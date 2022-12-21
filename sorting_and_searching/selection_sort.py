def selection_sort(arr):
    for space in range(len(arr)-1, 0, -1):
        max_index = 0
        for location in range(1, space+1):
            if arr[location] > arr[max_index]:
                max_index = location
        arr[space], arr[max_index] = arr[max_index], arr[space]
    return arr

print(selection_sort([5, 2, 4, 6, 1, 3]))

