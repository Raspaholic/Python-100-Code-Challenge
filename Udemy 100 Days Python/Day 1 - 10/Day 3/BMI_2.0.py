#BMI Calculator 2.0
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
print(str(round(BMI, 2)) + " is your BMI.")

if BMI < 18.5:
    print(f"Your BMI is {round(BMI, 2)}, you are underweight")
elif BMI < 25:
    print(f"Your BMI is {round(BMI, 2)}, you have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {round(BMI, 2)}, you are overweight")
elif BMI < 35:
    print(f"Your BMI is {round(BMI, 2)}, you are obese")
else:
    print(f"Your BMI is {round(BMI, 2)}, you are clinically obese")
