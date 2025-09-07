def conditions():
    n = []
    for i in range(1, 12):
        n.append(i)
    return n
    
    
con = conditions()
#print(con)


def while_loop():
    i = 1 
    while i < 15:
        print(i)
        i += 3
   
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
       
       
    

def check_even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    
def check_positive(num):
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print("The number is zero")
        
        
        
def reverse(char):
    result = ""
    for i in char:
        result = i + result
    return result

#print(reverse("ARCHIMEDES SENA SENADJU"))  

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_of_numbers(numbers, nums):
    total = 0
  #  while total < 100:
    for number in numbers:
        total += number
        if total >= nums:
            break
    return total

sum_result = sum_of_numbers(num, 10)
#print(f"The sum of numbers is: {sum_result}")



i = 20  
while i < 30:
    if i % 2 == 0:
        print(f"{i} is divisible by 3")
        i += 2
    else:        print(f"{i} is not divisible by 3")   
    break 