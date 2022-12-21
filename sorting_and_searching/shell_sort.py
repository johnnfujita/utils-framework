def shell_sort(arr):
    distance = len(arr) // 2
    while distance > 0:
        for i in range(distance, len(arr)):
            temp = arr[i]
            j = i
            while j >= distance  and arr[j - distance] > temp:
                arr[j] = arr[j - distance]
                print(distance, j)
                print(arr)
                j -= distance 
            arr[j] = temp
            print(arr)
        distance //= 2
    return arr

print(shell_sort([5, 2, 4, 6, 1, 3]))
