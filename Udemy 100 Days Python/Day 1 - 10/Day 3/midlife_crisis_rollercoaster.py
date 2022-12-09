height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
if height >= 120:
    if age < 12:
        print("You can ride!")
        print("Child tickets are $5")
        bill = 5
    elif age <= 18:
        print("You can ride!")
        print("Youth tickets are $7")
        bill = 7
    elif age > 18 and age < 45:
        bill = 12
        print("Adult tickets are $12")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a FREE ride on us!")
else:
    print("You're too short to ride the ride:(")

want_pics = input("Do you want to purchase photos? Y or N ")
if want_pics == str("Y"):
    bill += 3
    print(f"Your final total is ${bill}")
else:
    print(f"Your final total is ${bill}")