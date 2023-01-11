# Program menyalin file dengan extensi .txt

File1 = input()
File2 = input()

try:
    with open(f"{File1}.txt", "r") as origin:
        a = origin.read()
except:
    print('\nGagal')
else:
    with open(f"{File2}.txt", "w") as copy:
        copy.write(a)
    print('\nBerhasil!')