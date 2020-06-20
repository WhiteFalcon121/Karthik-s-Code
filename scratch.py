#t00171
def main(number):
    primes_list = [2, 3, 5, 7]
    newlist = []
    inlist = False
    num = 1
    for i in range(2, number):
        currentval = i
        for i in primes_list:
            if currentval in primes_list:
                inlist = True
            elif currentval % i != 0:
                num = num + 1
            if num == 5 or inlist == True:
                newlist.append(currentval)
                break
        num = 1
        inlist = False
    return newlist

number = 10
list1 = (main(number+1))
# 10 = 2*5
while number != 1:
    for i in list1:  # 2, 3
        if number%i == 0: # yes
            number = number/i # 3
            print(i) # 3
