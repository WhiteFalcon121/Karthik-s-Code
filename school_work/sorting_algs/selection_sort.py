def find_lowest(list_name):
    """This function finds the lowest value in a given list"""
    compars = 1
    lowest = list_name[0]
    for x in list_name:
        if compars == len(list_name):
            break
        if x < lowest:
            lowest = x
    return lowest

def selection_sort(list1, reverse):
    i = 0
    list2 = list(list1)
    for i in range(len(list1)):
        list2 = list1[i:]
        lowest = find_lowest(list2)
        lowest_index = list1.index(lowest)
        if lowest_index!= i:
            list1[i], list1[lowest_index] = list1[lowest_index], list1[i]
        i +=1

        newlist = []
        num = 0
        for i in list1:
            if list1.count(i) > 1 and i in newlist:
                list1.pop(num)
                list1.insert(list1.index(i)+1, i)
            newlist.append(i)
            num += 1
    if reverse == True:
        list1=list1[::-1]
    return list1

reverse = False
list1 = [5, 4, 3, 2, 1, 2, 5]
print(selection_sort(list1, True))
