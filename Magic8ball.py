import random 
x = ["Yes!", "No!", "Maybe?", "Decide for Yourself!", "No Comment.", "Never!", "Always!", "I can't answer that."]

print("Welcome to Magic 8 Ball!")
name = raw_input("What is your name? ") 
print("Hello!")
y = raw_input("What is your question for the Magic 8-Ball? ")
print("And your answer is...")
print(random.choice(x))

z = raw_input("Play again(y/n)? ")
if z == "y":
    print("Please rerun the program! :)")
elif z == "n":
    print("Have a good day :)")