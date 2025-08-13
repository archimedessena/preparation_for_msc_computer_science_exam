def conditions():
    n = []
    for i in range(1, 12):
        n.append(i)
    return n
    
    
con = conditions()
#print(con)


def while_loop():
    i = 0 
    while i < 15:
        print(i)
        i += 1
   
# Greeting friends 
def greet_friends(): 
    friends = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
    for friend in friends:
        print(f"Greetings, {friend}!")
        
   
    
    
#greet_friends()


def greetings_using_while_loop():
    #friends = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
    friends = [1, 3, 4, 5, 6, 7]
    num = 1
    while True:
      if 3 in friends:
          print("Found", friends[1])
      break
       
        
greetings_using_while_loop()