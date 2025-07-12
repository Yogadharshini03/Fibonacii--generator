def fibonacci(n):
    # Initialize first two numbers
    a, b = 0, 1
    # Print Fibonacci series up to n
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

# Get input from user
num = int(input("Enter a number to generate Fibonacci series up to: "))
fibonacci(num)
