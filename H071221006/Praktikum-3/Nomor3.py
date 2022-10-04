#Nomor3

harga = int(input(""))
uang = int(input(""))
kembalian = uang-harga

pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

if uang < harga:
    print("Inputan tidak valid")
else:
    for i in pecahan:
        x = kembalian // i
        kembalian = kembalian-(x*i)
        print(x, "uang Rp.", i)



   
