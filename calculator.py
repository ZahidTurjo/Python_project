import os
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b


operations_dict={
    "+":add,
    "-":minus,
    "*":multiply,
    "/":division
}
new_process=True
while new_process:

    number= float(input("Enter first number:"))
    for symbol in operations_dict:
        print(symbol)
    end_process=False    
    while not end_process:    
        op_symbol= input("enter a operation:")
        next_number=float(input("Enter the next number:"))

        calculator_function=operations_dict[op_symbol]
        output=calculator_function(number,next_number)
        print(output)

        should_continue=input(f"Enter 'y' to continue calculation with {output} or new calculation type 'n' and 'x' to exist:").lower()
        if should_continue == 'y':
            number=output
        elif should_continue == 'n':
              end_process=True
              os.system("cls")
        elif should_continue == 'x':
            end_process=True
            new_process=False
            print("Bye...") 

























