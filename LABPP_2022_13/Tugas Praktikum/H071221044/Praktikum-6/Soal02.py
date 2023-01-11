#2. Buatlah sebuah program untuk menyalin file dengan extensi .txt kemudian hasil salinannya ditulis kembali dengan format rata kanan.
filename = input() + ".txt"
n = int(input())

a = open(filename, "w")
try:
    for i in range(n):
        nama = input().replace(' ', '_')
        nim = input()
        angkatan = input()    
    
    a.write("+" + "-"*len(nama) + "+" + "-"*(len(nim)+2) + "+" + "-"*(len(angkatan)+5) + "+\n")
    a.write("|" + " Nama" + " "*(len(nama) - 5) + "|" + " NIM" + " "*(len(nim) -2 )+ "|" + " Angkatan" + " "*(len(angkatan)-4) + "|" + "\n")
    a.write("+" + "-"*len(nama) + "+" + "-"*(len(nim)+2) + "+" + "-"*(len(angkatan)+5) + "+\n")
    a.write("|" + nama + "| " + nim + " | " + angkatan + " "*4 +"|" + "\n")
    a.write("+" + "-"*len(nama) + "+" + "-"*(len(nim)+2) + "+" + "-"*(len(angkatan)+5) + "+")
    
    print("Berhasil")
except:
    print("Gagal")
    
a.close()