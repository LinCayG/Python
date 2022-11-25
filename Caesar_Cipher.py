alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(orig_text, shift_num):
    cipher_text = ""
    for i in orig_text:
        pos = alphabet.index(i)
        new_pos = pos+shift_num
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(de_text, de_shift):
    cipher_text = ""
    for i in de_text:
        pos = alphabet.index(i)
        new_pos = pos-de_shift
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    print(f"The decoded text is {cipher_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number(between 0 and 26):\n"))
    encrypt(orig_text=text,shift_num=shift)
elif direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number(between 0 and 26):\n"))
    decrypt(de_text=text,de_shift=shift)
else:
    print("Invalid input.")
