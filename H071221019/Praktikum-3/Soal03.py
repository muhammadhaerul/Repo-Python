harga = int(input("Harga Barang = "))
bayar = int(input("Nilai Uang yang Dibayarkan = "))
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if harga <= bayar:
    kembalian = bayar - harga
    print(f"Jumlah Kembalian = Rp. {kembalian:,}".replace(",","."))
    for i in uang_pecahan: 
        jumlah_pecahan= int(kembalian/i)
        kembalian = kembalian - (i * jumlah_pecahan)
        print(f"{jumlah_pecahan} uang Rp. {i:,}".replace(",",".")) 
else:
    print("Uang Tidak Cukup")


