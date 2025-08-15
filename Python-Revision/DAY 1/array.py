arr = [10, 20, 30, 40]
print(arr[1])  # O(1): 20
arr.append(50)  # O(1) amortized: [10, 20, 30, 40, 50]
arr.insert(2, 25)  # O(n): [10, 20, 25, 30, 40, 50]
arr.remove(30)  # O(n): [10, 20, 25, 40, 50]
index = arr.index(40)  # O(n): 3

x = 0
while x < len(arr):
    print(arr[x])  # O(n): prints each element
    x += 1
print(arr)  # Final array: [10, 20, 25, 40, 50]
print(len(arr))  # O(1): 5
print(arr[2:4])  # O(k): [25, 40] where k is the slice length
print(arr[-1])  # O(1): 50
print(arr[::-1])  # O(n): [50, 40, 25, 20, 10]
print(arr[1:])  # O(n): [20, 25, 40, 50]
print(arr[:3])  # O(3): [10, 20, 25]
print(arr[1:3])  # O(2): [20, 25]
print(arr[::2])  # O(n/2): [10, 25, 50]
print(arr[1::2])  # O(n/2): [20, 40]
print(arr[::-2])  # O(n/2): [50, 25, 20]
print(arr[1:4:2])  # O(2): [20, 40]
print(arr[::3])  # O(n/3): [10, 40]
print(arr[1::3])  # O(n/3): [20, 50]
print(arr[::-3])  # O(n/3): [50, 20]
print(arr[1:4:3])  # O(1): [20]
print(arr[::4])  # O(n/4): [10, 50]
print(arr[1::4])  # O(n/4): [20]
print(arr[::-4])  # O(n/4): [50, 10]
print(arr[1:5:4])  # O(1): [20]
print(arr[::5])  # O(n/5): [10]
print(arr[1::5])  # O(n/5): [20]
print(arr[::-5])  # O(n/5): [50]
print(arr[1:5:5])  # O(1): [20]
print(arr[::6])  # O(n/6): [10]
print(arr[1::6])  # O(n/6): [20]
print(arr[::-6])  # O(n/6): [50]
print(arr[1:5:6])  # O(1): [20]