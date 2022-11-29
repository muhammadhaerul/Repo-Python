namafile = input() + ".txt"
banyakasisten = int(input())
hasil = open(namafile, "w+")

try:
    hasil.write("+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 10 + "+\n")
    hasil.write("|" + " Nama" + " " * 17 + "|" + " NIM" + " " * 8 + "|" + " Angkatan" + " " + "|" + "\n")  
    hasil.write("+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 10 + "+\n") 

    for i in range(banyakasisten):
        nama = input().replace(" ", "_")
        if len(nama) > 20:
            print("Inputan nama tidak boleh lebih dari 20")
            raise TypeError()
        nim = input()
        angkatan = input()

        hasil.write("|" + " " + nama + " " * (22-(len(nama)+1)) + "| " + nim + " " * (12-(len(nim)+1)) + "| " + angkatan + " " * (10-(len(angkatan)+1)) + "|" + "\n")
    hasil.write("+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 10 + "+\n") 
    print("Berhasil")

except:
    print("Gagal")

hasil.close()