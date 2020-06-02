list1 = [3, 1, 4, 5, 2]
compars = 1

print(list1)

for i in range(0, len(list1)):
  lowest = list1[0]
  for x in list1:
    "print('compars is', compars)"
    if compars == len(list1):
      "print ('lowest is', lowest)"
      first_num = list1[0]
      if first_num > lowest:
        lowest_index = list1.index(lowest)
        list1[0] = lowest
        list1[lowest_index] = first_num
        print('new list1:', list1)
      compars = 1
      break
    next_index = list1.index(x) + 1
    print('x is', x)
    print(next_index)
    if list1[next_index] < x and list1[next_index] < lowest:
      lowest = list1[next_index]
      print('new lowest is', lowest)
    compars = compars + 1

print('is ordered into', list1)
