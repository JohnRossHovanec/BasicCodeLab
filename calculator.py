print("Easy Calc")

math_type = input("Would you like to do 1) Addition, 2) Subtraction, 3) Multiplication, or 4) Division? Please enter 1, 2, 3, or 4: ")

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

def addition_math():
    answer = num1 + num2
    print("Result:", answer)

def subtraction_math():
    answer = num1 - num2
    print("Result:", answer)

def multiplication_math():
    answer = num1 * num2
    print("Result:", answer)

def division_math():
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        answer = num1 / num2
        print("Result:", answer)

if math_type == '1':
    addition_math()
elif math_type == '2':
    subtraction_math()
elif math_type == '3':
    multiplication_math()
elif math_type == '4':
    division_math()
else:
    print("Invalid input. Please enter a valid choice.")
