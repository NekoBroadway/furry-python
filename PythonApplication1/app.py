#Exc 7 - Write a Python program to accept a filename from the user and print the extension of that

import os

path = input("Enter full path to file: ")

if os.path.exists(path):
    ex = os.path.basename(path).split(".") 
    print(f"Type of your file is \"{ex[1]}\"")
else:
    print("This file does not exists!")