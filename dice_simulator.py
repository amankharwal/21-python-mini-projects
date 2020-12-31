import random 
while True:     
     user = int(input("Choose One Option: \n1. roll the dice \n2. exit\n"))     
     if user==1:         
        number = random.randint(1,6)         
        print(number)     
     else:         
        break