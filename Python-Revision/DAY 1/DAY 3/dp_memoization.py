def fib_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print(fib_memo(50))  # Output: 12586269025 (fast)



#fib(5) checks memo -> Not found -> Computes fib(4) + fib(3)
#fib(4) stored in memo -> Reused later
#Only one call per n, linear time.