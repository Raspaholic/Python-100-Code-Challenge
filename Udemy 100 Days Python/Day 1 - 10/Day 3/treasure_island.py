print("Welcome to Treasure Island. Your quest is to find the treasure.")
lor = str(input("You're at a crossroad, where do you want to go; left or right? ")).lower()
if lor == str("right"):
    print("You fell into a hole. Game Over.")
else:
    print("You come to a lake. There is an island in the middle of the lake.")
    wos = str(input("Do you wait for a boat or do you swim across? wait | swim ")).lower()
    if wos == str("swim"):
        print("Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors: a red, a yellow, and a blue door.")
        wd = str(input("Which door do you choose? ")).lower()
        if wd == str("blue"):
            print("you enter a room of beasts. Game Over.")
        elif wd == str("red"):
            print("It's a room full of fire. Game Over.")
        elif wd == str("yellow"):
            print("You found the treasure! You win!")
