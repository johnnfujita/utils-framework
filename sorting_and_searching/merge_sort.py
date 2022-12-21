
passage = 0

def merge_sort(arr, passage):
    
    if len(arr) > 1:
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        passage += 1
        print("left", left, "pass", passage)
        
        print("right",right, "pass", passage)
        
        merge_sort(left, passage)
        merge_sort(right, passage)
        
        a = 0
        b = 0
        c = 0

        

        while a < len(left) and b < len(right):
            print(passage, "left", left, "right", right)
            if left[a] < right[b]:
                arr[c] = left[a]
                a += 1
            else:
                arr[c] = right[b]
                b += 1
            print("left and right pass")
            print(arr, "a", a, "b", b, "c", c)
            c += 1
           

        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1
            print("only left")
            print(arr, "a", a, "b", b, "c", c)

        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1
            print("only right")
            print(arr, "a", a, "b", b, "c", c)
    return arr


print(merge_sort([44, 16, 993, 12, 5, 93, 21, 28], passage))