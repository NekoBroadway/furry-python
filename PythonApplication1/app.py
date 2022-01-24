#Exc 5 - Write a Python program which accepts the user's first and last name and print them in reverse order with spaces between them

f_name = input("Enter your firstname: ")
l_name = input("Enter your lastname: ")

name = list()
name[:] = f_name + " " + l_name
name.reverse()

res = ""
print(res.join(name), end = "!\n")