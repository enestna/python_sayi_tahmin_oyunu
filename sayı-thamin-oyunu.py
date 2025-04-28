import random

def play():
    correct_number=random.randint(1,100)
    guess=None
    point=100
    print("Guess a number between 1 and 100")
    attempt_count=0
    while guess!=correct_number:
        guess=int(input("Please enter a guess number"))
        if guess<1 or guess>100:
            print("please enter a number between 1 and 100")
            continue
        if guess<correct_number :
            print("please enter a larger number: ")
            point-=10
            attempt_count+=1

        elif guess>correct_number :
            print("please enter a smaller number: ")
            point-=10
            attempt_count+=1

       
        if point==0:
            print("Sorry, you have no points left!")
            print(f"your {attempt_count}. try")

            break
        if guess==correct_number:
                attempt_count+=1
                print("Congratulations the number is correct")
                print(f"your {attempt_count}. try")
                print("your point=",point)

play()
