#t00171
def list_of_primes(number):
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

def main(number):
    list1 = (list_of_primes(number+1))
    returnlist = []
    # 10 = 2*5
    while number != 1:
        for i in list1:  # 2, 3
            if number%i == 0: # yes
                number /=i # 3
                returnlist.append(i) # 3
    return returnlist
print(main(121))
