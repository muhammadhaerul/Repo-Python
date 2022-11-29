def hitung_faktorial(nilai):
    if nilai >= 1:
        return nilai * hitung_faktorial(nilai - 1)
    elif nilai == 0:
        return 1
    else:
        return "Tidak Terdefinisi"

nilai = int(input("Masukkan nilai = "))
print(f"{nilai}! =",hitung_faktorial(nilai))