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
    
    print("You were headed to New York City in your private plane when you saw your pilot magically turn into a turtle as you flew over an island. With no one to steer, the plane crashes. You have survived the plane crash and are now on the mythical, forested island of Aurath with the pilot turtle as your companion. Your mission is to survive this island and complete the mystical wand of Aurath. You have found the wand lying on a rock, but 3 of the elemental stones are missing, and you must find them. Once you retrive all 3 and reinsert them into the wand, you will be returned home safely and gain the ability to turn into a dragon!!! Good luck!.") 
    
    food = int(40)
    health = int(50)
    magic = int(100)
    lives = int(1)
    water = int(40)
    medicine = int(40)
    time = int(530)
    
    inventory = ("You have %s life, %s health, %s magic, %s packets of food, %s canteens of water, and %s medical kits. The time is %s.")
    print(inventory %(lives, health, magic, food, water, medicine, time))
    while True:
        weapon= raw_input("What weapon would you like? bow and arrow, glaive, sword, or spear? ")
        if weapon == "bow and arrow": 
            print("You have choosen bow and arrow")
        elif weapon == "glaive": 
            print("You have choosen glaive")
        elif weapon == "sword": 
            print("You have choosen Sword")
        elif weapon == "spear":
            print("You have choosen spear")
        else:
            print("Please choose one of the options.")
        sure = raw_input("are you sure (y/n)? ")
        if sure == "n":
            print(("Too bad, you get it anyway! Congratulations, you got a " + weapon + "!"))
            break
        elif sure == "y":
            print("Congratulations, you got a " + weapon + "!")
            break
    print("Now that you have your supplies you are ready to begin your journey. Good luck dear adventurer, may luck be in your favor! ")    
   
    print("health: ", health)
    eat1 = raw_input("You are now mortally wounded because you crashed the plane. You must also care for the turtle or it will die. would you like a large, medium, small, or no health pack (l/m/s/n)? ")
    if eat1 == "l":
        medicine = 25
        health = 75
        print("health: ", health)
        print("medicine: ", medicine)
    elif eat1 == "m":
        medicine = 30
        health = 60
        print("health: ", health)
        print("medicine: ", medicine)
    elif eat1 == "s":
        medicine = 35
        health = 65
        print("health: ", health)
        print("medicine: ", medicine)
    elif eat1 == "n":
        print("health: ", health)
        print("medicine: ", medicine)
        print("YOU DIED!")
        end = raw_input("Play again (y/n)? ")
        if end == "y":
            print("Welcome back!")
            continue
        if end == "n":
            print("Goodbye!")
            break
   
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
        
   
    
        print("health: ", health)
    eat1 = raw_input("You are now hungry because you did not eat on the plane. would you like a large, medium, small, or no meal (l/m/s/n)? ")
    if eat1 == "l":
        food = 25
        health = 100
        print("health: ", health)
        print("food: ", food) 
        health = 85
        print("health: ", health)
        print("food: ", food)
    elif eat1 == "s":
        food = 35
        health = 80
        print("health: ", health)
        print("food: ", food)
    elif eat1 == "n":
        print("health: ", health)
        print("food: ", food)
        
    if path == "1":
        print("Now that you have eaten, you will be heading to the cave of Abysmal Den, but first you should learn the basics of your weapon in case you are attacked.")
    elif path == "2": 
        print("Now that you have eaten, you will be heading to the cave of Walslan Hole, but first you should learn the basics of your weapon in case you are attacked.")
    elif path == "3":
        print("Now that you have eaten, you will be heading to the Elmere caves, but first you should learn the basics of your weapon in case you are attacked.")
    
    
    print("You have now practiced for seven hours, you are thirsty and need to feed turtle.")
    
    print("health: ", health)
    drink1 = raw_input("would you like a large, medium, small, or no canteen (l/m/s/n)? ")
    if drink1 == "l":
        water = 0
        health = 100
        print("health: ", health)
        print("water: ", water)
    elif drink1 == "m":
        water = 5
        health = 85
        print("health: ", health)
        print("water: ", water)
    elif drink1 == "s":
        water = 8
        health = 80
        print("health: ", health) 
        print("water: ", water)
    elif drink1 == "n":
        print("health: ", health)
        print("water: ", water)
    
   
    
    if path == "1":
        print("You are now nearing a river.")
        player2= raw_input("Would you like to fill your canteens (y/n)? ")
        if player2 == "y":
            water = 15
            print("water: ", water)
        elif player2 == "n":
            print("water: ", water)
        print("Continuing on path. You finaly make it to the entrance of the cave and you enter. That is when you see a GIANT BEAR!!!!!!!!!!!")
        bear= raw_input("Would you like to fight, run, hide, or trick the bear(f/r/h/t)? ")    
        if bear == "f":
            print("You have successfully defeated the bear. The bear, understanding he was rightfully defeated in battle, presents you with the earth gem.")
        elif bear == "r":
            print("The bear easily catches up and eats you.")
            print("YOU DIED!")
            end = raw_input("Play again (y/n)? ")
            if end == "y":
                print("Welcome back!")
                continue
            if end == "n":
                print("Goodbye!")
                break
        elif bear == "h":
            print("The bear finds and kills you.")
            print("YOU DIED!")
            end = raw_input("Play again (y/n)? ")
            if end == "y":
                print("Welcome back!")
                continue
            if end == "n":
                print("Goodbye!")
                break
        elif bear == "t":
            print("You have successfully tricked the bear. The bear, understanding he was tricked, presents you with the earth gem.")
        path2 = raw_input("Now that you have claimed the gem you must choose a new path (2 or 3). ")
        if path2 == "2":
            print("You have chosen path 2.")
            print("you are nearing an apple tree.")
            player3= raw_input("Would you like to pick some apples (y/n)? ")
            if player3 == "y":
                food = 40
                print("food: ", food)
            elif player3 == "n":
                print("food: ", food)
       
        elif path2 == "3":
            print("You have chosen path 3.")
            print("You are nearing a mountain.")
            player4= raw_input("Would you like to climb the mountain (y/n)? ")
            if player4 == "y":
                print("You climbed the mountain and found the entrance to a cave. You then decide to enter and that is when you see a magma monster!!. you are frozen in fear for a second when you notice that behind this monster is the artifact, which is surrounded by a magic moat of lava")
                magma= raw_input("Would you like to fight, run, hide, or trick the monster?(f/r/h/t)")
                if magma== "f":
                    print("You have been toasted to a crisp.")
                    print("YOU DIED!")
                    end = raw_input("Play again (y/n)? ")
                    if end == "y":
                        print("Welcome back!")
                        continue
                    if end == "n":
                        print("Goodbye!")
                        break
                elif magma== "r":
                    print("You were hit by lava from behind.")
                    print("YOU DIED!")
                    end = raw_input("Play again (y/n)? ")
                    if end == "y":
                        print("Welcome back!")
                        continue
                    if end == "n":
                        print("Goodbye!")
                        break
                elif magma== "h":
                    print("you have been able to hide and sneak behind Magma. You silently jump across the moat and have collected the artifact.")
                
                elif magma == "t":
                    print("You have not tricked the monster so he threw you into the lava.")
                    print("YOU DIED!")
                    end = raw_input("Play again (y/n)? ")
                    if end == "y":
                        print("Welcome back!")
                        continue
                    if end == "n":
                        print("Goodbye!")
                        break
            elif player4 == "n":
                print("You will move around the mountain now.")

        
    elif path == "2":
        print("you are nearing an apple tree.")
        player3= raw_input("Would you like to pick some apples (y/n)? ")
        if player3 == "y":
            food = 40
            print("food: ", food)
        elif player3 == "n":
            print("food: ", food)
        print("You inching closer and closer to the cave and should get there tommorrow, but now you need to rest")
        
        print("Now that you are rested up you can continue the short journey to the cave. You finally have reached the cave when you hear a song. thats when you realize it is the infamous siren song.")
        siren= raw_input("Would you like to fight, run, hide, or co")
    elif path == "3":
        print("You are nearing a mountain.")
        player4= raw_input("Would you like to climb the mountain (y/n)? ")
        if player4 == "y":
            print("You climbed the mountain and found the entrance to a cave.")
        elif player4 == "n":
        el
        
    quit = raw_input("press Q to quit. ") 
    if quit == "Q" or "q":
        break    #so that the player can exit
    
    
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
    #has a villian at each cave to make it harder. Bear(will be guarding the earth), Siren(which will guard the water cave), A dragon (will guard the last cave) and a Magma monster (that will guard the fire element cave)
    #each cave has a gem and each gem is a different element. Water, Fire, Earth. 
    #Caves abysmal den, walslan hole, elmere caves
