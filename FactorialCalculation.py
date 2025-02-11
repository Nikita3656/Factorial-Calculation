def calculate_factorial(n):
    # Check if the number is negative
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    # Calculate the factorial using a loop
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

# Ask the user for input
number = int(input("Enter a non-negative integer to calculate its factorial: "))

# Calculate and print the factorial
result = calculate_factorial(number)
print(f"The factorial of {number} is: {result}")
