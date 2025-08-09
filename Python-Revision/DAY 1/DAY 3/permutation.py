from math import factorial
def permutation(n, r): # Arrangements(Order matters)
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)


def combination(n, r): # Selections(Order does not matter)
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))


perm = permutation(5, 2)
print(f"Permutation of 5P2: {perm}")