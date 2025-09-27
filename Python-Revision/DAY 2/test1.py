# To-do list manager
task = [] 
def add_task():
    ask = input("Do you want to add a task? (yes/no): ")
    while ask != "no":
        add_ = input("Add task: ")
        ask = input("Do you want to add a task? (yes/no): ")
        task.append(add_)
 
    #print(task)


def view(task):
    for i in task:
        print("Your tasks are: ", i)
   # print(task)
  
def remove_task(task):
    for i in task:
        task[i].pop()
    return task
        



def mark_as_done():
    pass
    
    
add_task()
view(task)