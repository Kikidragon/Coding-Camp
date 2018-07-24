import random
r = 1
p = 2
s = 3
rock = 4
paper = 5
scissors = 6
computer = ["rock!", "paper!", "scissors!"]
player = (input("Rock(r), Paper(p), or Scissors(s)? "))

if player == r:
    print("You chose rock!")
elif player == p:
    print("You chose paper!")
elif player == s:
    print("You chose scissors!")
else:
    print("Please choose either r, p, or s.")
    
print("The computer chose...")
print(random.choice(computer))


#doesn't work |
    
if player == r:
    if computer == 1:
        print("Tie!")
    elif computer == 2:
        print("You Lose!")
    elif computer == 3:
        print("You Win!")
elif player == p:
    if computer == 2:
            print("Tie!")
    elif computer == 3:
        print("You Lose!")
    elif computer == 1:
        print("You Win!")
elif player == s:
    if computer == 3:
        print("Tie!")
    elif computer == 1:
        print("You Lose!")
    elif computer == 2:
        print("You Win!")

#doesn't work either |

if player == computer:
    print("Tie!")
elif player == 1 and computer == "paper!":
    print("You Lose!")
elif player == 2 and computer == "scissors!":
    print("You Lose!")
elif player == 3 and computer == "rock!":
    print("You Lose!")
elif player == 2 and computer == "rock!":
    print("You Win!")
elif player == 1 and computer == "scissors":
    print("You Win!")
elif player == 3 and computer == "paper!":
    print("You Win!")
