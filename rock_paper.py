import random
score = 0
cpu = 0
while True:
    user = input("Choose between: Rock, Paper and Scissors  or e for Exit ")
    choices = ['rock','paper','scissors']
    if user.lower()==random.choice(choices):
        print("You Won!")
        score+=1
    elif user.lower()=='e':
        print("Thanks For Playing!!")
        print(f"Your Score Is: \nPlayer : CPU \n{score} : {cpu}")
        break
    else:
        print("You Lose")
        cpu+=1
