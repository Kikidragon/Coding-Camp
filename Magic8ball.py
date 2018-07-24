import random 
x = ["Yes!", "No!", "Maybe?", "Decide for Yourself!", "No Comment.", "Never!", "Always!", "I can't answer that."]

name = input("What is your name? ") 
print("Hello",name,"!")
print("What is your question for the Magic 8-Ball? ")
print("And your answer is...")
print(random.choice(x))
