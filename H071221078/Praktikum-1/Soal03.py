nama_seller = str(input("Nama Seller: "))
gaji_pokok = float(input("Gaji Pokok: "))
total_penjualan = float(input("Total Penjualan: "))

total_gaji = gaji_pokok + (total_penjualan*0.15)

print("TOTAL: $" ,round(total_gaji,2))