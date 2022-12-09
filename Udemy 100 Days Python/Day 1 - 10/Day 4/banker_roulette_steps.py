import random

print("Welcome to Banker Roulette where I choose who's paying everyone's bill.")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print(names)
num_items = len(names)
print(num_items)
random_choice = random.randint(0, num_items - 1)  # - 1 gives the last index of the list
person_paying = names[random_choice]
print(f"{person_paying} is the unfortunate winner.")
