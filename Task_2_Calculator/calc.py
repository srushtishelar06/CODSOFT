# Takes two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Displaying operation list
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the operation choice from user
operation = input("Choose operation (1/2/3/4): ")

# Performing calculation based on user choice
if operation == "1":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")    
elif operation == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "3":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

    # avoid division by zero
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: can't divide by zero")   
