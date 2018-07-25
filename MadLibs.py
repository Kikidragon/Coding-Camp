x = 0    #creates infinite loop!
while x == 0:
    print("Welcome to MadLibs! You will be asked to provide parts of speech to be put into a funny story. Have fun!")

    noun1 = raw_input("Noun? ")
    food = raw_input("Food? ")
    personinroom = raw_input("Person in room? ")
    emotion = raw_input("Emotion? ")
    pronoun = raw_input("Pronoun? ")
    adjective = raw_input("Adjective? ")
    madlibs = ("Once there was a %s who always ate %s. One day, %s broke in and stole all their food. The %s was so %s that %s went to get the food back. When %s arrived, %s found out that %s had taken the %s to make a surprise party for the %s. %s was so %s that %s gave %s a big hug!")
    print(madlibs %(noun1, food, personinroom, noun1, emotion, pronoun, pronoun, pronoun, personinroom, food, noun1, pronoun, adjective, pronoun, personinroom))
    reply = raw_input("Play again (y/n)? ")
    if reply == "n":
        break     #stops the program!

        

   
   