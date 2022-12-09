height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
if height >= 120:
    if age < 12:
        print("You can ride!")
        print("Your ticket price is $5")
        bill = 5
    elif age <= 18:
        print("You can ride!")
        print("Your ticket price is $7")
        bill = 7
    else:
        print("You can ride!")
        print("Your ticket price is $12")
        bill = 12
else:
    print("You're too short to ride the ride:(")

want_pics = input("Do you want to purchase photos? Y or N ")
if want_pics == str("Y"):
    bill += 3
    print(f"Your final total is ${bill}")
else:
    print(f"Your final total is ${bill}")