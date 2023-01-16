alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))
shift = shift % 26


def encrypt(plain_text, shift_amount):
    cypher = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cypher += new_letter
        else:
            cypher += letter
    print(f"the encoded text is {cypher}")


def decrypt(plain_text, shift_amount):
    cypher = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cypher += new_letter
        else:
            cypher += letter
    print(f'The decoded text is {cypher}')


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)



