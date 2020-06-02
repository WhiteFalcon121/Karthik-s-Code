list1 = [5, 2, 3, 1, 4]
list2 = []
compars = 1

print(list1)

while len(list1) != 0:
  lowest = list1[0]
  for x in list1:
    "print('compars is', compars)"
    if compars == len(list1):
      "print ('lowest is', lowest)"
      list1.remove(lowest)
      list2.append(lowest)
      "print('List1:', list1, 'List2:', list2)"
      compars = 1
      break
    next_index = list1.index(x) + 1
    "print('x is', x)"
    "print(next_index)"
    if list1[next_index] < x and list1[next_index] < lowest:
      lowest = list1[next_index]
      "print('new lowest is', lowest)"
    compars = compars + 1

print('is ordered into', list2)
