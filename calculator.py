print("Simple Calculator")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


a = get_number("Enter first number: ")
b = get_number("Enter second number: ")     

# Available operations
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Prompt the user to select an operation choice
choice = input("Enter choice (1/2/3/4): ")

# Perform the appropriate calculation
if choice == '1':
    print("Result:", a + b)
elif choice == '2':
    print("Result:", a - b)
elif choice == '3':
    print("Result:", a * b)
elif choice == '4':

    # Check for division by zero to prevent program crash
    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", a / b)

  # Handle any invalid menu choices
else:
    print("Invalid choice")
       
       