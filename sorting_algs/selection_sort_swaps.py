def find_lowest(list_name):
    """This function finds the lowest value in a given list"""
    compars = 1
    lowest = list_name[0]
    for x in list_name:
        if compars == len(list_name):
            break
        next_index = list_name.index(x) + 1
        if list_name[next_index] < x and list_name[next_index] < lowest:
            lowest = list_name[next_index]
        compars += 1
    return lowest

list1 = [5, 4, 3, 2, 1, 2, 5]
# find lowest, swap it
# find lowest in sublist

print('Sorting this list:', list1)

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

print('Result: ', list1)
