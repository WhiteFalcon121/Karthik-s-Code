string1 = 'AB'
string1 = 'ABC'
before = string1
after = []
all = ['A', 'B', 'AB', 'BA']
all2 = ['A', 'B', 'C', 'AB', 'BA', 'BC', 'CB', 'CA', 'AC', 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
all3 = ['A', 'B', 'C', 'AB', 'AC', 'BA', 'BC', 'CA', 'CB']#ADD ON MISSING LETTER TO 2s
# find all permutations of substrings
# 0 = A, 1 = B
# 0, 1, 01, 10

#for i in before:
    #after.append(i)

print(after)

print(len(before))
