print("Hello World")
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")
print("Hello" + " " + "World!")

print("What is your name?")
input("What is your name?")
print("Hello " + input("What is your name?")) #input() allows for user input: str, num, bool

iLength = input()
print(len(iLength)) #len() returns the number of items in an object: if obj is str len() returns number of char

name = input("What is your name?")
print(name)

lName = len(input("What is your name | age"))
print(lName)

n = input("What is your name?")
print(n)

greeting = "Hello! "
city = input("What city did you grow up in?")
petName = input("What's your pet's name?")

bandName = greeting + city + petName + " " + "is your band name!"
print(bandName)