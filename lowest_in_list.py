def find_lowest(list_name):
    compars = 1
    lowest = list_name[0]
    for x in list_name:
        #print('compars:', compars)
        #print('x: ', x)
        if compars == len(list_name):
            break
        next_index = list_name.index(x) + 1
        #print('next_index: ', next_index)
        #print('next one is: ', list_name[next_index])
        if list_name[next_index] < x and list_name[next_index] < lowest:
            lowest = list_name[next_index]
        compars += 1
    return lowest
