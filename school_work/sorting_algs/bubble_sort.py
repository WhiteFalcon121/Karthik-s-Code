list1 = [1, 3, 4, 5, 2, 7, 8, 9, 10]
print(list1)

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

  print(list1)
