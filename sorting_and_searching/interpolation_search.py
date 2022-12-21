def interpolation_search(arr, target):
    low = 0
    high = len(arr)-1
    found = False
    while low <= high and not found:
        mid = low + int(((float(high-low)/(arr[high]-arr[low])) * (target-arr[low])))

        if arr[mid] == target:
            found = True
            return found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return found


print(interpolation_search([1,2,3,4,5,6,20], 3))