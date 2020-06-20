def bubble_sort(list1, reverse):
    for i in range(0, len(list1)-1):
      for x in list1:
        next_index = list1.index(x) + 1
        if next_index == len(list1):
          break
        'print(next_index)'
        next_one = list1[next_index]
        if x > next_one:
          list1[next_index] = x
          list1[list1.index(x)] = next_one
        print(list1)

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
list1 = [5, 2, 3, 1, 4, 14, 0.3, 2, 4, 2, 4]
print(bubble_sort(list1, True))
