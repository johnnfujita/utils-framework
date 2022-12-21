def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    found = False
    while low <= high and not found:
        print(low, high)
        mid = (low + high) // 2
        print(mid)
        if arr[mid] == target:
            found = True
            
        else:
            if target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
    return found



print(binary_search([1,2,3,4,5,6,20], 20))