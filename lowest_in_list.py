def find_lowest(list_name):
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
