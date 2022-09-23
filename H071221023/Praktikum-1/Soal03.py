wh = float(input ("rata-rata pemakain listrik harian (wh): "))

## mengubah wh ke kwh ##
harian = float(wh/1000)
bulanan = float(harian * 30)
harga = float(bulanan * 1325)

print("jumlah tagihan listrik bulanan : RP.", round(harga, 2))  