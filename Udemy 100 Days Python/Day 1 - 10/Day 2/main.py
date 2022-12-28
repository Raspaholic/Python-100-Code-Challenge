#Data Types:

#String
    print("Hello, world!")
#selecting certain letter of string using brackets and printing results
    print("Hello"[1])#counts up from 0 not starting at 1
#Subscripting: pulling certain element from string
    print("Hello"[4])

#Integer (negative or positive whole numbers are all integers)
    print(123 + 456)
#Writing large numbers can be separated with '_' instead of comma i.e: 789_541_120
    print(123_456_789)

#Float (negative or positive numbers with decimal values)
    pi = 3.14159
    print(pi)

#Boolean (only two values: True or False has to be capitalized)
    poop = True
    print(poop)
    pee = False
    print(pee)


    num_char = len(input("What is your name?"))
    new_num_char = str(num_char) #converts num_char to string
    print("Your name has " + new_num_char + " characters.") #The result has all the same data type now (strings)
#type() function checks the data type that's inside the parenthensis and puts the type in the console

#can change a data type to other data types
    a = 123
    b = str(123)
    c = float(123)
    d = bool(123)
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))

    print(70 + float("100.5")) #converts string to float and adds integer

    two_digit_number = input("Type a two digit number: ")
    digit_one = two_digit_number[0]
    digit_two = two_digit_number[1]
    result = int(digit_one) + int(digit_two)
    print(result)

#Mathmatical Operations in Python (follows PEMDAS + LR)
#Parenthensis, Exponents, Multiplication, Division, Addition, Subtraction, Left, Right
add = 1 + 2
sub = 2 - 1
mult = 2 * 1
div = 4 / 2 #gives float result
raised_exponent = 2 ** 2

#BMI Calculator = Weight(kg) / height^2(m^2)
height_ft_str = input("How many feet tall are you?")
height_in_str = input("How many inches added with feet tall are you?")
weight_lbs_str = input("How much do you weight in pounds?")
height_ft = int(height_ft_str)
height_in = float(height_in_str)
height_ft_cm_m = (height_ft * 30.48) / 100
height_in_cm_m = (height_in * 2.54) / 100
final_height_m = height_ft_cm_m + height_in_cm_m
weight_lbs = float(weight_lbs_str)
weight_lbs_g_kg = (weight_lbs * 453.592) / 1000
BMI = weight_lbs_g_kg / (final_height_m ** 2)
print(str(height_ft_cm_m) + " meters tall from feet.")
print(str(height_in_cm_m) + " meters tall from inches.")
print(str(final_height_m) + " meters tall.")
print(str(weight_lbs_g_kg) + " weight in kilograms.")
print(str(BMI) + " is your BMI.")

#Number Manipulation and F Strings in Python
print(8/3)
print(int(8/3))
print(round(8/3)) #can specify number of digits of precision to round to round(8/3, 2) rounding to 2 digits after decimal
print(round(8/3, 2))
print(round(2.66666666, 2))
#division in Python always gives float data type by default
print(8//3)
#floor division returns only whole numbers
result = 4/2 #equals 2
result /= 2 #divides result and sets the result to the variable by 2
print(result)

score = 0
score += 1
print(score)

#f-Strings (makes it easy to mix strings and different data types)
score1 = 1
height = 1.8
isWinning = True
print(f"your score is {score1}, your height is {height}, you're winning: {isWinning}")

current_age = input("What is your age?")
years_left = 90 - int(current_age)
days_left = years_left * 365
weeks_left = years_left * 52.1428571
months_left = years_left * 12
message = f"You have {years_left} years left, {months_left} months left, {weeks_left} weeks left, {days_left} and days left until you reach the age of 90."
print(message)

#Tip/Bill Splitter Calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, 15, or a custom tip? "))
num_people = int(input("How many people to split the bill? "))
total_tip = float(((total_bill / 100) / (percentage / 100))) #150.84 with 10% tip
total_aftr_tip = total_bill + total_tip
result = total_aftr_tip / num_people
print(round(result, 2))