# Program menyalin file dengan extensi .txt dan hasil salinannya ditulis kembali menggunakan format rata kanan

F1 = input()
F2 = input()

try:
    with open(f"{F1}.txt","r") as file1:
        x = file1.readlines()
except:
    print("\nGagal")
else:
    panjang = 0
    for i in x:
        if len(i) > panjang:
            panjang = len(i)
    with open(f"{F2}.txt","w") as file2:
        for i in x:
            file2.write(f"{i.rjust(panjang)}")
    print("\nBerhasil!")