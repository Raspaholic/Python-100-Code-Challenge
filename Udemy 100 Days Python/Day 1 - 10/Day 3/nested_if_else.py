height = int(input("What is your height in cm?"))
age = int(input("How old are you?"))
if height >= 120:
    if age < 12:
        print("You can ride the rollercoaster!")
        print("Your ticket price is $5")
    elif age <= 18:
        print("You can ride the rollercoaster!")
        print("Your ticket price is $7")
    else:
        print("You can ride the rollercoaster!")
        print("Your ticket price is $12")
else:
    print("You can't ride:(")
