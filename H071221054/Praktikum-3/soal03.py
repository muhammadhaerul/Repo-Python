print('Program Menghitung Kembalian Uang dari Suatu Transaksi')
print('------------------------------------------------------')

x = int(input( )) #harga
y = int(input( )) #bayar

n = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if x <= y:
    k = y - x
    print(f"Jumlah Kembalian = Rp. {k:,}".replace(",","."))
    for i in n: 
        pembagian_kembalian = k//i
        k = k - (i * pembagian_kembalian)
        print(f"{pembagian_kembalian} uang Rp. {i:,}".replace(",",".")) 
else:
    print("Uang Tidak Cukup")