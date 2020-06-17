list1 = [2, 5, 0, 9.5]
num1 = 0

print('Sorting this list:', list1)

for x in list1:
  numsbefore = list1.index(x)
  currentnum = x
  if numsbefore != 0:
    for x in list1[:numsbefore]:
      "print('Checking sublist:', list1[:numsbefore])"
      "print(currentnum)"
      if currentnum < x:
        num1 = num1 + 1
      if num1 == len(list1[:numsbefore]):
        "print('Putting', currentnum, 'at beginning of list')"
        list1.remove(currentnum)
        list1.insert(0, currentnum)
        num1 = 0
        continue
      if currentnum < x and list1.index(currentnum) > list1.index(x):
        "print(currentnum, 'is less than', x)"
        list1.remove(currentnum)
        list1.insert(list1.index(x), currentnum)
        "print(list1)"
    num1 = 0
    
  newlist = []
  num = 0
  for i in list1:
    if list1.count(i) > 1 and i in newlist:
      list1.pop(num)
      list1.insert(list1.index(i)+1, i)
    newlist.append(i)
    num += 1

print('Result:', list1)
