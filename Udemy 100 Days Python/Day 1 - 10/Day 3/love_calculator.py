print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n") #\n is new line
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_str = combined_string.lower() #makes whole string lower cased
#.count checks for that letter in the string
t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e = lower_case_str.count("e")

true = t + r + u + e

l = lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e = lower_case_str.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like idk pancakes and syrup")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you're alright together")
else:
    print(f"Your score is {love_score}")
print(love_score)
