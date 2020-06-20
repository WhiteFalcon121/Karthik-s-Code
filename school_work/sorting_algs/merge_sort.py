def merge_sort(list_name):
    if len(list_name) > 1:
        mid = len(list_name)//2
        left = list_name[:mid]
        right = list_name[mid:]
        print(left, right)
        # recursive
        merge_sort(left)
        merge_sort(right)

        # to go through halves
        i = 0
        j = 0

        # to go through main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_name[k] = left[i]
                i+=1
            else:
                list_name[k] = right[j]
                j+= 1
            k+=1

        while i < len(left):
            list_name[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            list_name[k] = right[j]
            j+=1
            k+=1
    return list_name

list1 = [2, 3, 7, 1, 5, 2, ]
print(merge_sort(list1))
