# Program menyalin biodata asisten Pengantar Pemrograman

a = input()
with open(f"{a}.txt","w") as item:
    item.write("+----------------------+------------+----------+\n")
    item.write("| Nama                 | NIM        | Angkatan |\n")
    item.write("+----------------------+------------+----------+\n")

try:
    with open(f"{a}.txt","a") as file:
        n = int(input())
        for i in range(n):
            nama = str(input())
            if len(nama) > 20:
                print("Panjang nama tidak boleh lebih dari 20 Karakter")
                raise Exception()
            NIM = str(input())

            if len(NIM) > 10:
                print("NIM harus kurang dari 10 karakter")
                raise Exception()
            angkatan = str(input())

            if len(angkatan) > 4:
                print("Tahun harus 4 karakter")
                raise Exception()
            
            file.write(f"| {nama.ljust(20)} | {NIM.ljust(10)} | {angkatan.ljust(8)} |\n")
        file.write("+----------------------+------------+----------+")
        print("\nBerhasil!")
except:
    print("\nGagal")