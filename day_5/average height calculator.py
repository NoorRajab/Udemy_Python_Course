ages_as_csv = input("Please insert all the heights of the students seperated by a comma: ")
ages_list = ages_as_csv.split(",")
list_length = len(ages_list)
heights_int = [int(h) for h in ages_list]
total_height = 0
for height in heights_int:
    total_height += height
average_height = round(total_height/list_length)
print(f"Average height of the {list_length} students is {average_height}cm")    
