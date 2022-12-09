import random

print("Welcome to Heads or Tails, time to test your luck.")
usr_choice = str(input("What do you say, heads or tails? "))

random_side = random.randint(0, 1)
if random_side == 1:
    if usr_choice == str("heads"):
        print("Your choice was right, you flipped heads!")
    else:
        print("Your choice was wrong, the coin is heads")
else:
    if usr_choice == str("tails"):
        print("Your choice was right, you flipped tails!")
    else:
        print("Your choice was wrong, the coin is tails")
