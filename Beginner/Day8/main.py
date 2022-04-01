alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_encrypt):
    result = ""
    for letter in plain_text:
        index_letter = alphabet.index(letter)
        index_shift = index_letter + shift_encrypt
        while index_shift > len(alphabet):
            index_shift -= len(alphabet)
        result += alphabet[index_shift]
    print(f"The encoded text is {result}")


def decode(encrypted_text, shift_decode):
    result = ""
    for letter in encrypted_text:
        index_letter = alphabet.index(letter)
        index_shift = index_letter - shift_decode
        result += alphabet[index_shift]
    print(f"The decoded text is {result}")


again = "yes"

while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decode(text, shift)
    else:
        print("ERROR!!! Type 'encode' or 'decode'.")

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
