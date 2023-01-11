import os

filecopy = input("Nama file yang di copy: ") + ".txt"
filetarget = input("Nama file hasil: ")

target = os.path.isfile(filecopy)

if target == False:
    print("Gagal")
    exit()

with open(filecopy, "r") as file:
    with open(filetarget+".txt", "w") as hasil: 
        for i in file:
            hasil.write(i)