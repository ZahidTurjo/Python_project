import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['!','@','$','%','^','&','*','(',')','-','+']

print("Welcome to the password generator")
n_letters=int(input("How many letters u want in the password?\n"))
n_symbols=int(input("How many symbols u want in the password?\n"))
n_numbers=int(input("How many numbers u want in the password?\n"))

password=""
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password=password+char
print(password)    

for i in range(1,n_symbols+1):
    sym=random.choice(symbols)
    password=password+sym
print(password)    

for i in range(1,n_numbers):
    int=random.choice(numbers)
    password=password+int
print(password)    
