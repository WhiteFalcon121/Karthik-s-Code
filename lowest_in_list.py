def find_lowest(list_name):
  compars = 1
  lowest = list1[0]
  for x in list_name:
    if compars == len(list_name):
      break
    next_index = list1.index(x) + 1
    if list_name[next_index] < x and list_name[next_index] < lowest:
      lowest = list_name[next_index]
    compars = compars + 1
  return lowest

list1 = [2, 5, 1, 10, 1]
print(find_lowest(list1))
