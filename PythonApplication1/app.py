#Exc 10 - Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = input("Enter an integer (n): ")
res = int(n) + int(n + n) + int(n + n + n)

print(f"{n} + {n}{n} + {n}{n}{n} = {res}")