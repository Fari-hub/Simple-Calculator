#Simple Calculator that handles numbers and strings😇
def calculator():
    print("Welcome to the Simple Calculator💖!")
    print("You can add➕, subtract ➖, multiply ✖️, or divide ➗numbers and also join text.")
    print("Example input: 5 + 5 or 'Happy' + 'Coding'")
    
    # Get user input
    first = input("Enter the first value: ")
    operator = input("Enter the operator (+, -, *, /): ")
    second = input("Enter the second value: ")

    # Converting to numbers
    try:
        num1 = float(first)
        num2 = float(second)

        # Perform arithmetic
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                result = float('nan')
            else:
                result = num1 / num2
        else:
            result = "Invalid operator for numbers."

    except ValueError:
        # If conversion fails, treat them as strings
        if operator == '+':
            result = first + second
        elif operator == '*':
            try:
                times = int(second)
                result = first * times
            except ValueError:
                result = "Error: Can't multiply a string unless the second value is a number."
        else:
            result = "This operation is not supported for text."

    print("Result:", result)

# Run the calculator
calculator()
