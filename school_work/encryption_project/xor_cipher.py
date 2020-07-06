''''
key = 10100111 #random binary with 8 characters here
message = "abc"
list1 = []
list2 = []
list3 = []
for i in message:
    list1.append(ord(i)) # convert to ascii
    '''
#for i in list1:
    #list2.append(bin(i)[2:]) # convert to binary
    '''
print(list1)
for i in list1:
    list3.append((bin(int(i)^key))[2:])
print(list3)
''''''
