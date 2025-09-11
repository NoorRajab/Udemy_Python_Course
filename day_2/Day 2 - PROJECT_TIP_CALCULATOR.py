print("*****TIP CALCULATOR*****\n________________________")
bill = float(input("What was the bill: $"))
tip_percentage = int(input("What percentage would you liike to give 10,12,15: "))
bill_tip = (tip_percentage/100)*bill
total_bill_with_tip = bill_tip + bill
people = int(input("How many people to split the bill: "))
bill_per_person = float(round(total_bill_with_tip/7,2))
print(f"Each person should pay: {bill_per_person}")