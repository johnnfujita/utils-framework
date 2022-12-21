# GOOD FOR PARTIALLY SORTED DATA

def insertion_sort(arr):
    # iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # set j to the index of the be one less than the current iteration of i
        j = i-1
        # ith element is going to be the next element in the array (this is the element we are trying to insert)
        next_item = arr[i]

        # we will start inserting the next item until we find the correct spot for it, if we reach -1, we know we have inserted it at the beginning
        while j >= 0 and arr[j] > next_item:
            # shift the arr[j] element to the right by one
            arr[j+1] = arr[j]
            # decrement j by one
            j -= 1
            # this works actually by progressively comparing the decrmenting jth item to the next item which is the one we want to insert

        # Here is the point where next item is finally greater than the previous item, so we insert it here, or we have reached the beginning
        arr[j+1] = next_item
    return arr

print(insertion_sort([5, 2, 4, 6, 1, 3]))