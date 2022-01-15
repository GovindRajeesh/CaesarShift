whites=[
    " ",
    "\n"
]

def encrypt(text,key,white=False):
    encrypted=""

    for letter in text:
        letter_to_asci=ord(letter)

        encrypted+=chr(letter_to_asci+key)

    if not white:
        for c in whites:
            encrypted=encrypted.replace(chr(ord(c)+key),c)

    return encrypted

def decrypt(text,key,white=False):
    decrypted=""

    for letter in text:
        letter_to_asci=ord(letter)

        decrypted+=chr(letter_to_asci-key)

    if not white:
        for c in whites:
            decrypted=decrypted.replace(chr(ord(c)-key),c)

    return decrypted