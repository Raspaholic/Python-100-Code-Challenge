import random #a python module
import my_module

#module
random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.pi) #use . whatever to call something in another module or python program

#random floating point number
random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is: {love_score}")
