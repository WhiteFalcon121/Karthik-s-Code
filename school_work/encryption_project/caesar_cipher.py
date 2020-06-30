import random
key = random.randint(0, 26) #inclusive range
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S,' 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

plaintext = str(input("What message would you like to encrypt?").upper())
print(plaintext)
