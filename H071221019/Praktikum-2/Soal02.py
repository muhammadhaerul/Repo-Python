# Program menginput informasi daya listrik dan menghitung total tagihan listrik

golongan = input("Golongan = ")
daya = int(input("Daya = "))
pemakaian = float(input("Pemakaian = "))

match golongan:
    case "R1":
        if daya == 900:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1352:_}".replace('.',',').replace('_','.'))
        elif daya == 1300:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1444.70:_}".replace('.',',').replace('_','.'))
        elif daya == 2200:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1444.70:_}".replace('.',',').replace('_','.'))
        else:
            print("> Data Tidak Valid")
    case "R2":
        if daya >= 3500 and daya <= 5500:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1699.53:_}".replace('.',',').replace('_','.'))
        else:
            print("> Data Tidak Valid")
    case "R3":
        if daya >= 6600:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1699.53:_}".replace('.',',').replace('_','.'))
        else:
            print("> Data Tidak Valid")
    case "B2":
        if daya >= 6600 and daya <= 200000:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1444.70:_}".replace('.',',').replace('_','.'))
        else:
            print("> Data Tidak Valid")
    case "B3":
        if daya > 200000:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1114.74:_}".replace('.',',').replace('_','.'))
        else:
            print("> Data Tidak Valid")
    case "I3":
        if  daya >= 200000:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1314.12:_}".replace('.',',').replace('_','.'))
        else:
            print("> Data Tidak Valid")
    case "P1":
        if daya >= 6600 and daya <= 200000:
            print(f"> Jumlah Tagihan Anda : Rp {pemakaian * 1523.28:_}".replace('.',',').replace('_','.'))
        else:
            print("> Data Tidak Valid")
    case other:
        print("> Data Tidak Valid")