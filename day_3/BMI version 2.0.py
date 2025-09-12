print("*****Body Mass Index Version 2.0*****\n_____________________________________")
weight = float(input("How much do you weigh: "))
height = float(input("What is your height: "))
BMI = round(weight/(height**2))

if BMI < 18.5:
    print(f"Your BMI is {BMI},you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {BMI},you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {BMI},you are overweight.")
elif BMI <=35:
    print(f"Your BMI is {BMI},you are obese.")
else:
    print(f"Your BMI is {BMI},you are clinically obese.")