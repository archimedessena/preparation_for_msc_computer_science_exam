arr = [10, 20, 30, 40]
print(arr[1])  # O(1): 20
arr.append(50)  # O(1) amortized: [10, 20, 30, 40, 50]
arr.insert(2, 25)  # O(n): [10, 20, 25, 30, 40, 50]
arr.remove(30)  # O(n): [10, 20, 25, 40, 50]
index = arr.index(40)  # O(n): 3