
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None
    
    def add_task(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def show_tasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.task)
            current = current.next
        return tasks

# Usage
todo = ToDoList()
todo.add_task("Do laundry")
todo.add_task("Buy groceries")
todo.add_task("Call mom")
print(todo.show_tasks())  