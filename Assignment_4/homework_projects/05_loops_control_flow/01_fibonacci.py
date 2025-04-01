MAX_VALUE = 10000  # Constant for the maximum value

def fibonacci_sequence():
    a, b = 0, 1
    while a < MAX_VALUE:
        print(a, end=" ")
        a, b = b, a + b  # Update to the next terms

# Run the function to print Fibonacci sequence
fibonacci_sequence()
