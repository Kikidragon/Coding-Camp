import random
import time

x = 0    #creates infinite loop!
while x == 0:
    print("") #opening here/welcome message
    
    #what variables should we make?
    
    name= raw_input("What is your name? ")
    print("Hello", name)
    gender = raw_input("What is your gender (b/g)? ")
    if gender == "b":
        boygirl = "boy"
    elif gender == "g":
        boygirl = "girl"
    print("You are a", boygirl)
    
    print("You have survived a plane crash and are now on the mythical, forested island of Aurath. Your mission is to survive this island and find the mystical wand of Aurath. Once you retrive this item you will be returned home safely and gain the ability to turn into a dragon!!! Good luck!.") 
    
    food = 40
    health = 100
    magic = 100
    lives = 3
    water = 40
    medicine = 40
    time = 530
    
    inventory = ("You have %s lives, %s health, %s magic, %s packets of food, %s canteens of water, and %s medical kits. The time is %s.")
    print(inventory %(lives, health, magic, food, water, medicine, time))
    weapon= raw_input("What weapon would you like? bow and arrow, glave, sword, or spear?")
    if weapon == "bow and arrow": 
        print("You have choosen bow and arrow")
    elif weapon == "glave": 
        print("You have choosen glave")
    elif weapon == "sword": 
        print("You have choosen Sword")
    elif weapon == "spear":
        print("You have choosen spear")
    
    #STORY NOTES:
    #in a forest on an island "Aurath", 
    #plane crash,
    #can make weapons, 
    #choose if a boy or girl, 
    #cannibals/wild animals,
    #3 lives, 
    #no villian only bad situation, 
    #retrieving magic artifact (turns them into a dragon!!!:), 
    #magic (elemental),
    #characters can starve, die of thirst, have to sleep, get sick, etc.,
    #different seasons with different resources,
    #can choose name,
    #different foods have different health benefits,
    #animal helpers,
    #make time???
    #multiple characters???
    #1 or 2 players???
        
    quit = raw_input("press Q to quit. ") 
    if quit == "Q" or "q":
        break    #so that the player can exit
    
