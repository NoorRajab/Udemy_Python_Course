import random 

test_seed = int(input("Please input a test_seed number: "))
random.seed(test_seed)
names_as_csv = input("Please insert the names f the peple responsible seperated by a comma: ")
namesCSV = names_as_csv.split(",")
randm = random.randint(0,4)
chosen_name = namesCSV[randm]
print(f"{chosen_name} will pay the bill")