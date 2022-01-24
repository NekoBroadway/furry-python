#Exc 6 - Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

seq = input("Enter some number separated with commas: ")

my_list = seq.split(", ")

my_tuple = tuple(my_list)

print(f"List - {my_list}")
print(f"Tuple - {my_tuple}")