alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(ci_text, shift_num, ci_direction):
    cipher_text = ""
    if ci_direction == "decode":
        shift_num *=-1
    for char in ci_text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos+shift_num
            cipher_text += alphabet[new_pos]
        else:
            cipher_text +=char

    print(f"The {ci_direction}d text is {cipher_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(ci_text=text,shift_num=shift, ci_direction=direction)
    result = input("Type 'yes' if you want to go again.  Otherwise type 'no'.\n")
    if result =="no":
        should_continue = False
        print("Thanks and have a great day!")

