list_of_numbers_CVS = input("Please insert a list of numbers seperated by a comma: ").split(",")
list_of_numbers = [int(n) for n in list_of_numbers_CVS]
largest_number = 0
for num in list_of_numbers:
    if num > largest_number:
        largest_number = num
print(f"The largest number is {largest_number}")