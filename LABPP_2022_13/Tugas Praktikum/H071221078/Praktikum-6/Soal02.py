import os

targetcopy = input("File yang akan dicopy : ") + ".txt"
hasilcopy = input("Nama file setelah di copy: ") + ".txt"
cekfile = os.path.isfile(targetcopy)

if cekfile == True:
    print("Berhasil")

else:
    print("Gagal")
    exit()

panjangawal = 0
file = open(targetcopy)
for i in (file):
    if len(i.rstrip()) > panjangawal:
        panjangawal = len(i.rstrip())
file.close()

file = open(targetcopy)
banyakbaris = len(file.readlines())
baris = 1
file.close()

with open(targetcopy, "r") as hasil:
    copy = open(hasilcopy, "w")
    for isi in hasil:
        if baris < banyakbaris:
            text = f"{isi.rstrip():>{panjangawal}}\n"
        
        else:
            text = f"{isi.rstrip():>{panjangawal}}"
        copy.write(text)
        baris += 1