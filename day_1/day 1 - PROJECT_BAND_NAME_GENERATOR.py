print("*****WELCOME TO BAND NAME GENERATOR*****"+"\n________________________________")
city_name=input("What's name of the city you grew up in?\n")
pet_name=input("What's your pet's name?\n")
city_length=len(city_name)
pet_length=len(pet_name)
if city_length>pet_length:
    print("Your band name could be: "+pet_name+" "+city_name)
else:
    print("Your band name could be: "+city_name+" "+pet_name)
