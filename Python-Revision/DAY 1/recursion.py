# More complex recursion example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
    
    
result = factorial(3)
print(f"The factorial is: {result}")


# More complex recursion example
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    
result1 = fibonacci(5)
print(f"The 5th Fibonacci number is: {result1}")