# Tugas Praktikum 2 pekan 2

golongan = str(input("Masukkan golongan : "))
daya = float(input("Masukkan daya listrik (VA): "))
pemakaian = float(input("Masukkan pemakaian listrik : "))

if golongan == 'R1':
    if daya == 900 :
        print (f"Jumlah tagihan : {pemakaian*1352:,}")
    elif daya >= 1300 and daya <= 2200 :
        print (f"jumlah tagihan : {pemakaian*1400.70:,}")
    else :
        print("Invalid Data")
elif golongan == 'R2':
    if daya >= 3500 and daya <= 5500 :
        print (f"Jumlah tagihan : {pemakaian*1699.53:,}")
    else :
        print("Invalid Data")
elif golongan == 'R3':
    if daya >= 6600 :
        print (f"Jumlah tagihan : {pemakaian*1699.53:,}")
    else :
        print("Invalid Data")
elif golongan == 'B2':
    if daya >= 6600 and daya <= 200000 :
        print (f"Jumlah tagihan : {pemakaian*1444.70:,}")
elif golongan == 'B3':
    if daya >= 20000 :
        print (f"Jumlah tagihan : {pemakaian*1444.74:,}")
    else :
        print("Invalid Data")
elif golongan == 'I3':
    if daya >= 20000 :
        print (f"Jumlah tagihan : {pemakaian*1314.12:,}")
    else :
        print("Invalid Data")
elif golongan == 'P1':
    if daya >= 6600 and daya <= 200000 :
        print (f"Jumlah tagihan : {pemakaian*1314.12:,}")
    else :
        print("Invalid Data")
else:
    print("Invalid Data")
