from collections import deque

queue = deque()
queue.append(10)  # O(1): deque([10])
queue.append(20)  # O(1): deque([10, 20])
queue.append(30)  # O(1): deque([10, 20, 30])
print(queue[0])  # O(1): 10
print(queue.popleft())  # O(1): 10, deque([20, 30])
print(queue.popleft())  # O(1): 20, deque([30])