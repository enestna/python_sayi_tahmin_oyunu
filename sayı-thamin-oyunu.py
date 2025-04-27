import random

def play():
    correct_number=random.randint(1,100)
    guess=None
    point=100
    print("Guess a number between 1 and 100")

    while guess!=correct_number:
        guess=int(input("Please enter a guess number"))
        if guess<correct_number and guess>=1 and guess<=100:
            print("please enter a larger number")
            point-=10
        elif guess>correct_number and guess>=1 and guess<=100:
            print("please enter a smaller number")
            point-=10
        else:
            print("please enter a number between 1 and 100")
        if point==0:
            print("Sorry, you have no points left!")
            break
    print("Congratulations the number is correct")
    print("your point",point)

play()
