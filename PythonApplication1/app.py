import random as r

def genRandFloats(path, size):
    with open(path, "w") as sFile:
        for i in range(size):
            n1 = int(r.random() * pow(10, r.randint(1, 100)))
            n2 = int(r.random() * pow(10, r.randint(1, 100)))
            
            if (i % 2 == 0):
                n3 = n1 + n2
            else:
                n3 = n1 + n2 + 1 

            form = "{};{};{}\n".format(n1, n2, n3)
            sFile.write(form)

def compareFileNumbers(path):
    with open(path, "r") as sFile:
        t = 0
        f = 0

        num_list = sFile.read().split("\n")

        for i in range(len(num_list)):
                num_list[i] = num_list[i].split(";")

        for i in range(len(num_list) - 1):
            if int(num_list[i][0]) + int(num_list[i][1]) == int(num_list[i][2]):
                t += 1
            else:
                f += 1

        print(f"TRUE - {t}")
        print(f"FALSE - {f}")

file1 = "lorem1.txt"
file2 = "lorem2.txt"
file3 = "lorem3.txt"
file4 = "lorem4.txt"

genRandFloats(file1, 100)
genRandFloats(file2, 1000)
genRandFloats(file3, 10000)
genRandFloats(file4, pow(10, 6))


compareFileNumbers(file1)
compareFileNumbers(file2)
compareFileNumbers(file3)
compareFileNumbers(file4)