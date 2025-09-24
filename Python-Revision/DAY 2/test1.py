# To-do list manager
def add_task():
    task = [] 
    add = input("Add task: ")
    task.append(add)
    return task
    
    
                
   # while task_1 < 10:
   #     task_for_the_day = input("Enter your task for the day: ")
   #     task.append(task_for_the_day)
   #     task_1 +=1 
   #     break
   # return task 


def view():
    tasks = add_task()
    print(tasks)
    
    
    
add_task()
view()