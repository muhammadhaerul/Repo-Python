#Nomor3

usia = int(input(""))

def myDay(usia):
    tahun = (usia // 360)
    bulan = (usia % 360 // 30)
    hari = (usia % 360 % 30)

    print(tahun, "tahun")
    print(bulan, "bulan")
    print(hari, "hari")

myDay(usia)



