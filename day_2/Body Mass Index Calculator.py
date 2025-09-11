print("*****BODY MASS INDEX CALCULATOR*****\n____________________________________")
height = float(input("What is your height: "))
weight = float(input("What is your weight: "))
height_squared = height*height
Body_Mass_index =int( weight/height_squared)
print(f"Your Body Mass Index is : {Body_Mass_index}")