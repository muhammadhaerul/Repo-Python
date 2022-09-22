#Nomor3

print("Menghitung total gaji seller")

nama = input("Masukkan nama: ")
gaji_pokok = float(input("Masukkan gaji pokok: "))
total_penjualan = float(input("Masukkan total penjualan: "))
total = round(15/100 * total_penjualan + gaji_pokok, 2)

print("Total gaji: ",'$',total)
