import random

print("So you've finally woken up. We are the only surviors, everyone else died.")
    
def game_start():    
    print("So, what should we do? I dont know much about surviving on a deserted island.")
    print("-1-ask them who they are")
    print("-2-fight")
    print("-3-find food and water")
    print("-4-find shelter")

game_start()

if input() == ("1"):
    print("What do you mean? You dont remember me?")
    print("I guess you must have hit your head hard. I am Oric Ocean-Born. You were the captain of the ship before Joriek betrayed us by selling out our location to the black beards.")
    print("-1-ask why all the names are so stupid")
    print("-2-ask who the black beards are.")

    if input() == ("1"):
        print("Don't disrespect me, even though your my captain I will still slaughter you without batting an eyelid.")
        game_start()

        if input() == ("2"):
            print("The black beards are the meanest pirates in the seas")
            game_start()

elif input() == ("3"):
    print("Alrighty matey, I found this tasty fruit while your were asleep")
    print("*Eats it")
    print("*Dies")
    

# comment

