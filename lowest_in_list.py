def find_lowest(list_name):
    compars = 1
    lowest = list_name[0]
    for x in list_name:
        if compars == len(list_name):
            break
        if x < lowest:
            lowest = x
    return lowest
list1  = [9, 5, 1, 6, 1, 23]
print(find_lowest(list1))
