import random


playerhealth = 100
health = 50


#ATTACK FUNCTION

def attack_enemy(health):
    global playerhealth

    while health > 0 and playerhealth > 0:
        print("-1-kick")
        print("-2-punch")
        print("-3-backflip torpedo whirlwind strike")
        attack_option = input()
    #Kick
    
        if attack_option == ("1"):
            if random.randint(1,100)<90:
                print("You delt 10 damage!")
                health = health - 10
                print("Enemy is at", health, "hp")
                    
                if health < 1:
                    print("The enemy has been defeted")
                    victory = True
        
                else:
                    playerhealth = playerhealth - random.randint(10,20)
                                    
                    if playerhealth < 1:
                        print("You have died!")
                        exit()
                    
                    else:
                        print("You have been hit")
                        print("You are now at", playerhealth, "hp")
                        
            else:
                print("Your attack was blocked!")
                playerhealth = playerhealth - random.randint(10,25)
                    
                    
                if playerhealth < 1:
                        print("You have died!")
                        exit()
                    
                else:
                    print("You have been hit")
                    print("You are now at", playerhealth, "hp")
        
    #Punch
        
        elif attack_option == ("2"):
            if random.randint(1,100)<70:
                print("You delt 20 damage!")
                health = health - 20
                print("Enemy is at", health, "hp")
                    
                if health < 1:
                    print("The enemy has been defeted")
                    victory = True

                    
                else:
                    playerhealth = playerhealth - random.randint(10,20)
                    
                    
                    if playerhealth < 1:
                        print("You have died!")
                        exit()
                    
                    else:
                        print("You have been hit")
                        print("You are now at", playerhealth, "hp")

            else:
                print("Your attack was blocked!")
                playerhealth = playerhealth - random.randint(10,25)
                    
                    
                if playerhealth < 1:
                        print("You have died!")
                        exit()
                    
                else:
                    print("You have been hit")
                    print("You are now at", playerhealth, "hp")

    #Baclflip Torpedo Whirlwind Strike

        elif attack_option == ("3"):
            if random.randint(1,100)<35:
                print("You delt 50 damage!")
                health = health - 50
                print("Enemy is at", health, "hp")
                    
                if health < 1:
                    print("The enemy has been defeted")
                    victory = True

                    
                else:
                    playerhealth = playerhealth - random.randint(10,20)
                    
                    
                    if playerhealth < 1:
                        print("You have died!")
                        exit()
                    
                    else:
                        print("You have been hit")
                        print("You are now at", playerhealth, "hp")

            else:
                print("Your attack was blocked!")
                playerhealth = playerhealth - random.randint(10,25)
                    
                    
                if playerhealth < 1:
                        print("You have died!")
                        exit()
                    
                else:
                    print("You have been hit")
                    print("You are now at", playerhealth, "hp")

    



print("You've finally woken up. We are the only surviors, everyone else died.")
    
def game_start():    
    print("So, what should we do? I dont know much about surviving on a deserted island.")
    print("-1-ask them who they are")
    print("-2-fight")
    print("-3-find food and water")
    print("-4-find shelter")
    what2do = input()



    if what2do == ("1"):
        print("What do you mean? You dont remember me?")
        print("I guess you must have hit your head hard. I am Oric Ocean-Born. You were the captain of the ship before Joriek betrayed us by selling out our location to the black beards.")
        print("-1-ask why all the names are so stupid")
        print("-2-ask who the black beards are.")

        what2do = input()
        
        if what2do == ("1"):
            print("Don't disrespect me, even though your my captain I will still slaughter you without batting an eyelid.")
            game_start()

        elif what2do == ("2"):
            print("The black beards are the meanest pirates in the seas")
            game_start()

    elif what2do == ("2"):
        health = 60
        print("Oric Ocean-Born has", health, "hp")
        attack_enemy(60)
        print("You now wonder what to do next")
        print("-1-Find food and water")
        print("-2-Find shelter")
            
        what2do = input()
        if what2do == ("1"):
            print("You find a large bees nest, but wont be able to extract anything without a fight.")
            print("-1-Fight the bees")
            print("-2-Continue searching.")
            what2do = input()

            if what2do == ("1"):
                health = 75
                print("Swarm of bees have", health, "hp")
                attack_enemy(75)
                print("You eat the honey, and it causes your health to regenerate.")
                global playerhealth
                playerhealth = playerhealth + 100
                print("You now search for some water")
                crab()

            elif what2do == ("2"):
                crab()
        
        elif what2do == ("2"):
            shelter()
                




    elif what2do == ("3"):
        print("Alrighty matey, I found this tasty fruit with purple spots while your were asleep")
        print("*Eats it*")
        print("*Dies*")
        print("Without your friend, you search for food, making sure not to eat fruit with purple spots.")

        crab()

    elif what2do == ("4"):
        print("Alright then, I will just eat this suspiciously tasty fruit")
        print("*Dies*")
        print("Without your friend, you search for shelter, making sure not to eat suspicious food.")
        shelter()


def crab():
    
    print("You come across a flowing river that leads into a large lake, but your instincts tells you to be cautios.")
    print("-1-Drink the water")
    print("-2-Jump in the lake")


    what2do = input()

    if what2do == ("1"):
                print("You drink the water, and it soothes your bones, replenishing your health and making you feel stronger, but you still need to find food.")
                global playerhealth
                playerhealth = playerhealth + 100
                print("-1-Search for food")
                print("-2-Search for shelter")
                what2do = input()
                
                if what2do == ("1"):
                    food()

                elif what2do == ("2"):
                    shelter()



    elif what2do == ("2"):
        print("A large crab grabs you and throws you out of the river.")
        health = 300
        print("Large crab has", health, "hp")
        attack_enemy(300)


def shelter():
    print("After searching, you find a cave, but it looks a bit dangerous")
    print("-1-Explore")
    print("-2-Find food instead")
    what2do = input()

    if what2do == ("1"):
        print("In the darkness, you are attacked by giant spiders")
        health = 80
        print("Spiders have", health, "hp")
        attack_enemy(80)
        print("At the end of the tunnel you find an unusual looking apple and eat it")
        print("It makes you feel more powerful, increasing current health by 150")
        global playerhealth
        playerhealth = playerhealth + 150
        print("The apple does make you feel thirsty, so you search for water.")
        crab()


    elif what2do == ("2"):
        food()
            
def food():
    print("The only food you can find has purple spots and looks suspiciously tasty.")
    print("-1-Eat fruit")
    print("-2-Find Shelter")
    what2do = input()

    if what2do == ("1"):
        print("You ate the fruit and felt a strange feeling.")
        print("You fall to the ground, gasping for breath")
        print("The fruit has blocked your airways and you have died")
        exit()

    elif what2do == ("2"):
        shelter()


#comment
game_start()