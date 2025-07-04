#Create a program that takes two numbers from the user 
# and performs a basic arithmetic operation (addition, subtraction, multiplication, or division) based on their choice.

exit_program = True
print("test")
while exit_program == True:
    num1 = int(input ("Give a number"))
    num2 = int(input ("Give another number"))
    operation = input("Select an operation")
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)
    elif operation == 'exit':
        exit_program = False
    else:
        print("Wrong choice")
        