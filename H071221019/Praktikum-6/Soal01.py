file01 = input()
file02 = input()
try:
    with open(f"{file01}.txt","r") as file1:
        data = file1.read()
except:
    print("Gagal")
else:
    with open(f"{file02}.txt","w") as file2:
        file2.write(data)
    print("Berhasil")
