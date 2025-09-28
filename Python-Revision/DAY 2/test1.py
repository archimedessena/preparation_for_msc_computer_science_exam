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
  
             
def remove_task(tasks):
    while True:
        ask = input("Do you want to remove any task? (yes/no): ").lower()
        if ask == 'no':
            break
        elif ask == 'yes':
            task_name = input("Enter the task you want to remove: ")
            if task_name in tasks:
                tasks.remove(task_name)
                print(f"Task '{task_name}' removed successfully!")
            else:
                print("Task not found")
        else:
            print("Please enter 'yes' or 'no'")
    
    print("Updated task list:", tasks)           
       
def mark_as_done():
    pass
    
    
add_task()
view(task)
remove_task(task)