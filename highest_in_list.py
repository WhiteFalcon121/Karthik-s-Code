def find_highest(list_name):
    compars = 1
    highest = list_name[0]
    for x in list_name:
        if compars == len(list_name):
            break
        if x > highest:
            highest = x
    return highest

list1 = [2, 2, 10, 4, 51, 1, 3, 5, 25]
print(find_highest(list1))
