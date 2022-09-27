golongan = input("golongan = ")
daya = float(input("daya = "))
pemakaian = float(input("Pemakaian = "))

if golongan == "R1" :
    if daya == 900:
        harga = "Jumlah tagihan anda : {:_}".format(pemakaian*1352)
        print(harga.replace(".",",").replace("_","."))
    elif daya==1300 or daya==2200 :
        harga = "Jumlah tagihan anda : {:_}".format(pemakaian*1400.70)
        print(harga.replace(".",",").replace("_","."))
    else :                                                
        print ("Data tidak valid")
elif golongan == "R2" :
    if daya>=3500 and daya<=5500 :
        harga = "Jumlah tagihan anda : {:_}".format(pemakaian*1699.53)
        print(harga.replace(".",",").replace("_","."))
    else :
        print("Data tidak valid")
elif golongan == "R3":
    if daya>=6600:
        harga = "Jumlah tagihan anda : {:_}".format(pemakaian*1699.53)
        print(harga.replace(".",",").replace("_","."))
    else :
        print('Data tidak valid')
elif golongan == "B2":
    if daya>=6600 and daya<=200000 :
        harga = "Jumlah tagihan anda : {:_}".format(pemakaian*1444.70)
        print(harga.replace(".",",").replace("_","."))
    else :
        print("Data tidak valid")
elif golongan == "B3" :
    if daya>200000 :
        harga = "Jumlah tagihan anda : {:_}".format(pemakaian*1114.74)
        print(harga.replace(".",",").replace("_","."))
    else :
        print("Data tidak valid")
elif golongan == "I3" :
    if daya>=200000 :
        harga = "Jumlah tagihan anda : {:_}".format(pemakaian*1314.12)
        print(harga.replace(".",",").replace("_","."))
    else :
        print("Data tidak valid")
elif golongan == "P1" :
    if daya>=6600 and daya<=200000 :
        harga = "Jumlah tagihan anda : {:_}".format(pemakaian*1314.12)
        print(harga.replace(".",",").replace("_","."))
    else :
        print("Data tidak valid")
else :       
    print ("Data tidak valid")

