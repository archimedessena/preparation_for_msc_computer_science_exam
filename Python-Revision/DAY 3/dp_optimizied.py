def fib_tab_optimized(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fib_tab_optimized(50))  # Output: 12586269025


#Table: [0, 1, 1, 2, 3, 5, ...]
#Fill from index 0 to n, each step adds previous two values.
#Optimized version keeps only prev and curr variables.