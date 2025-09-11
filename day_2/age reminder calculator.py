age_as_int = int(input("What is your current age: "))
age_difference_in_60yrs = 60 - age_as_int
days_remaining = age_difference_in_60yrs*365
weeks_remaining = age_difference_in_60yrs*52
print(f"You are remaining with {age_difference_in_60yrs} years, {weeks_remaining} weeks and {days_remaining}")