print("=" * 25)
x = input()
with open(f"{x}.txt","w") as item:
    item.write("+----------------------+------------+----------+\n")
    item.write("| Nama                 | NIM        | Angkatan |\n")
    item.write("+----------------------+------------+----------+\n")

try:
    with open(f"{x}.txt","a") as file:
        n = int(input())
        for i in range(n):
            nama= str(input())
            if len(nama) > 20:
                print("Nama harus tidak lebih dari 20 karakter")
                raise Exception()
            nim= str(input())
            if len(nim) > 10:
                print("NIM harus kurang dari 10 karater")
                raise Exception()
            angkatan= str(input())
            if len(angkatan) > 4:
                print("Tahun harus 4 karakter")
                raise Exception()
            file.write(f"| {nama.ljust(20)} | {nim.ljust(10)} | {angkatan.ljust(8)} |\n")
        file.write("+----------------------+------------+----------+")
        print("=" * 25)
        print("Berhasil")
        print("=" * 25)
except:
    print("Gagal")

