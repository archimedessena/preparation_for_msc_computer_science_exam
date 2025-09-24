class Stack():
    def __init__(self):
        self.items = []
        
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.items:
            return "It is an empty list"
        else:
            self.items.pop()
            
    
    def peek(self):
       return self.items[-1]
        
        
        
        
        
stack = Stack()
stack.push("task1")
stack.push("task2")
stack.push("task3")
stack.push("task4")
stack.push("task5")
print(stack.items)
print(stack.peek())
#stack.pop()

    
    
    
