import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(plaintext):
    key = random.randint(0, 25) #inclusive range - if it was 26, the letter would be the same
    ciphertext = []
    for i in plaintext:
        alphabet_index = alphabet.index(i)
        new_key = alphabet_index + key
        if new_key >= 26:
            new_key = (alphabet_index + key) - 26
        print(new_key)
        ciphertext.append(alphabet[new_key])
    ciphertext = ("".join(ciphertext))
    return ciphertext, key

message = str(input("What message would you like to encrypt?").upper())
print(encrypt(message))
