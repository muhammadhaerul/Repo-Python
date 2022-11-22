file01 = input()
file02 = input()
try:
    with open(f"{file01}.txt","r") as file1:
        data = file1.readlines()
except:
    print("Gagal")
else:
    panjang = 0
    for i in data:
        if len(i) > panjang:
            panjang = len(i)
    with open(f"{file02}.txt","w") as file2:
        for i in data:
            file2.write(f"{i.rjust(panjang)}")
    print("Berhasil")
