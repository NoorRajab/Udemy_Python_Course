height = round(float(input("Please give your height: ")),2)
if height >=120:
    print("You can ride the rollercoster")
    age = int(input("How old are you: "))
    if age < 12:
        print("Please pay $5.00")
    elif age <=18:
        print("Please pay $7.00")
    else:
        print("Please pay $10.00")
else:
    print("Please wait until you gain some height before you can ride the rollercoster.")
print("Thank you for your petronage")