def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

print(fib_naive(5))  # Output: 55 (but slow for large n)


#fib(5) calls fib(4) + fib(3)
#fib(4) calls fib(3) + fib(2), etc.
#Tree of calls grows exponentially, recomputing fib(3) multiple times.