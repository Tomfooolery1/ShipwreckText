import random

playerhealth = 100
health = 50

#ATTACK FUNCTION

def attack_enemy():
    global health
    global playerhealth
    print("-1-kick")
    print("-2-punch")
    print("-3-backflip torpedo whirlwind strike")
    attack_option = input()
 #Kick
 
    if attack_option == ("1"):
        if random.randint(1,100)<80:
            print("You delt 10 damage!")
            health = health - 10
            print("Enemy is at", health, "hp")
                
            if health < 1:
                print("The enemy has been defeted")
    
            else:
                playerhealth = playerhealth - random.randint(10,20)
                                
                if playerhealth < 1:
                    print("You have died!")
                
                else:
                    print("You have been hit")
                    print("You are now at", playerhealth, "hp")
                    attack_enemy()
                    
        else:
            print("Your attack was blocked!")
            playerhealth = playerhealth - random.randint(10,25)
                
                
            if playerhealth < 1:
                    print("You have died!")
                
            else:
                print("You have been hit")
                print("You are now at", playerhealth, "hp")
                attack_enemy()
    
#Punch
    
    elif attack_option == ("2"):
        if random.randint(1,100)<60:
            print("You delt 20 damage!")
            health = health - 20
            print("Enemy is at", health, "hp")
                
            if health < 1:
                print("The enemy has been defeted")

                
            else:
                playerhealth = playerhealth - random.randint(10,20)
                
                
                if playerhealth < 1:
                    print("You have died!")
                
                else:
                    print("You have been hit")
                    print("You are now at", playerhealth, "hp")
                    attack_enemy()

        else:
            print("Your attack was blocked!")
            playerhealth = playerhealth - random.randint(10,25)
                
                
            if playerhealth < 1:
                    print("You have died!")
                
            else:
                print("You have been hit")
                print("You are now at", playerhealth, "hp")
                attack_enemy()

#Baclflip Torpedo Whirlwind Strike

    elif attack_option == ("3"):
        if random.randint(1,100)<20:
            print("You delt 50 damage!")
            health = health - 50
            print("Enemy is at", health, "hp")
                
            if health < 1:
                print("The enemy has been defeted")

                
            else:
                playerhealth = playerhealth - random.randint(10,20)
                
                
                if playerhealth < 1:
                    print("You have died!")
                
                else:
                    print("You have been hit")
                    print("You are now at", playerhealth, "hp")
                    attack_enemy()

        else:
            print("Your attack was blocked!")
            playerhealth = playerhealth - random.randint(10,25)
                
                
            if playerhealth < 1:
                    print("You have died!")
                
            else:
                print("You have been hit")
                print("You are now at", playerhealth, "hp")
                attack_enemy()

    



print("So you've finally woken up. We are the only surviors, everyone else died.")
    
def game_start():    
    print("So, what should we do? I dont know much about surviving on a deserted island.")
    print("-1-ask them who they are")
    print("-2-fight")
    print("-3-find food and water")
    print("-4-find shelter")

game_start()

what2do = input()

if what2do == ("1"):
    print("What do you mean? You dont remember me?")
    print("I guess you must have hit your head hard. I am Oric Ocean-Born. You were the captain of the ship before Joriek betrayed us by selling out our location to the black beards.")
    print("-1-ask why all the names are so stupid")
    print("-2-ask who the black beards are.")

    if what2do == ("1"):
        print("Don't disrespect me, even though your my captain I will still slaughter you without batting an eyelid.")
        game_start()

    elif what2do == ("2"):
        print("The black beards are the meanest pirates in the seas")
        game_start()

elif what2do == ("2"):
    health = 60
    print("Oric Ocean-Born has", health, "hp")
    attack_enemy()




elif what2do == ("3"):
    print("Alrighty matey, I found this tasty fruit while your were asleep")
    print("*Eats it*")
    print("*Dies*")

# comment

