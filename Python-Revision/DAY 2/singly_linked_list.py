class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):  # O(n)
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, data):  # O(n)
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    def print_list(self):  # O(n)
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.print_list()  # 10 -> 20 -> 30 -> None
sll.delete(20)
sll.print_list()  # 10 -> 30 -> None