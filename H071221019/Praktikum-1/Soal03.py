# Menghitung jumlah tagihan untuk pemakaian listrik bulanan

nilai = int(input("Rata-rata pemakaian listrik harian (Wh): "))

harian_Kwh = float(nilai/1000)  # Mengubah Wh ke Kwh
bulanan = float(harian_Kwh * 30)
tagihan = float(bulanan * 1325) 

print("Jumlah tagihan listrik bulanan : Rp. %0.2f" % tagihan)
