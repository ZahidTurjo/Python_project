alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']

def encryption(plain_text,shift_key):
    chiper_text=''

    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift_key
            if new_position>25:
                chiper_text+=alphabet[new_position-26]
            else:
                chiper_text+=alphabet[new_position]
        else:
            chiper_text+=char
    
        
    print(chiper_text)    

def decryption(plain_text,shift_key):
    decrypt_text=''
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            old_position=position-shift_key
            if old_position<0:
                decrypt_text+=alphabet[old_position+26]
            else:
                decrypt_text+=alphabet[old_position]
        else:
            decrypt_text+=char
        print(decrypt_text)
wanna_end=False
while not wanna_end:
    what_to_do=input("Type 'encrypt' for encryption ,type 'decrypt' for decription:\n")
    text=input("Type your text: \n").lower()
    shift=int(input("type shift key: \n"))
    if what_to_do == "encrypt":
        encryption(text,shift)
    elif what_to_do == 'decrypt':
        decryption(text,shift)
    type=input("enter 'yes' if you stop the proces and enter 'no' to continue the process \n")
    if type == "yes":
        wanna_end=True
        print("have a nice day ..")
