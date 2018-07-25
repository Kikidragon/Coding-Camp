import random
import time
y = 0
x = 0    #creates infinite loop!
while x == 0:
    print("") #opening here/welcome message
    
    #what variables should we make?
    
    name= raw_input("What is your name? ")
    print("Hello " + name)
    gender = raw_input("What is your gender (b/g)? ")
    if gender == "b":
        boygirl = "boy"
    elif gender == "g":
        boygirl = "girl"
    print("You are a " + boygirl)
    
    print("You have survived a plane crash and are now on the mythical, forested island of Aurath. Your mission is to survive this island and complete the mystical wand of Aurath. You have found the wand lying on a rock, but 3 of the elemental stones are missing, and you must find them. Once you retrive all 3 and reinsert them into the wand, you will be returned home safely and gain the ability to turn into a dragon!!! Good luck!.") 
    
    food = 40
    health = 100
    magic = 100
    lives = 3
    water = 40
    medicine = 40
    time = 530
    
    inventory = ("You have %s lives, %s health, %s magic, %s packets of food, %s canteens of water, and %s medical kits. The time is %s.")
    print(inventory %(lives, health, magic, food, water, medicine, time))
    while True:
        weapon= raw_input("What weapon would you like? bow and arrow, glaive, sword, or spear? ")
        if weapon == "bow and arrow": 
            print("You have choosen bow and arrow")
        elif weapon == "glaive": 
            print("You have choosen glave")
        elif weapon == "sword": 
            print("You have choosen Sword")
        elif weapon == "spear":
            print("You have choosen spear")
        else:
            print("Please choose one of the options.")
        sure = raw_input("are you sure (y/n)? ")
        if sure == "y" or "n":
            print(("Too bad, you get it anyway! Congratulations, you got a " + weapon + "!"))
            break
    print("Now that you have your supplies you are ready to begin your journey. Good luck dear adventurer, may luck be in your favor! ")    
   
    path = raw_input("Which path would you like to take (1, 2, or 3)? ")
    if path == "1":
        print("You have chosen path 1.")
    elif path == "2":
        print("You have chosen path 2.")
    elif path == "3":
        print("You have chosen path 3.")
    if path == "1":
        print("you are on your way to the earth elemental artifact.")
    elif path == "2":
        print("you are on your way to the water elemental artifact.")
    elif path == "3":
        print("You are on the way to the fire elemental artifact.")
        
    health -15
    print("health: " + health)
    eat1 = raw_input("You are now hungry. would you like a large, medium, small, or no meal (l/m/s/n)? ")
    if eat1 == "l":
        food -15
        health +15
        print("health: " + health)
        print("food: " + food)
     if eat1 == "m":
        food -15
        health +15
        print("health: " + health)
        print("food: " + food)
        
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
    #has a villian at each cave to make it harder. Evil Unicorn(earth), Siren(which will gaurd the water cave), A dragon (will gaurd)
    #each cave has a gem and each gem is a different element. Water, Fire, Earth. 
    
    
    
        
    quit = raw_input("press Q to quit. ") 
    if quit == "Q" or "q":
        break    #so that the player can exit
    
