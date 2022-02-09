import random as r

def genRandFloats(path, size):
    with open(path, "w") as somefile:
        for i in range(size):
            n1 = r.random() * 1000000
            n2 = r.random() * 1000000
            n3 = r.random() * 1000000
            form = "{};{};{}\n".format(n1, n2, n3)
            somefile.write(form)

file1 = "lorem1.txt"
file2 = "lorem2.txt"
file3 = "lorem3.txt"

genRandFloats(file1, 100)
genRandFloats(file2, 1000)
genRandFloats(file3, 10000)