import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(plaintext):
    key = random.randint(0, 25) #inclusive range - if it was 26, the letter would be the same
    ciphertext = []
    for i in plaintext:
        if i in alphabet:
            alphabet_index = alphabet.index(i)
            new_key = alphabet_index + key
            if new_key >= 26:
                new_key = (alphabet_index + key) - 26
            ciphertext.append(alphabet[new_key])
        else:
            ciphertext.append(i) # for special characters
    ciphertext = ("".join(ciphertext))
    return ciphertext, key

def decrypt(ciphertext, key):
    plaintext = []
    for i in ciphertext:
        if i in alphabet:
            alphabet_index = alphabet.index(i)
            real_index = alphabet_index - key
            if real_index < 0:
                real_index = 26 + real_index
            plaintext.append(alphabet[real_index])
        else:
            plaintext.append(i)
    plaintext = ("".join(plaintext))
    return plaintext

def main():
    option = str(input("Decrypt or encrypt? (d or e)"))
    if option == "D" or option == "d":
        ciphertext = input("Enter ciphertext: ").upper()
        key = int(input("Enter key: "))
        print(decrypt(ciphertext, key))
    elif option == "E" or option == "e":
        message = str(input("Enter message to be encrypted: ").upper())
        print(encrypt(message))
    else:
        print("Not an option.")
