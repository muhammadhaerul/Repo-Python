def myDay(usia):
    tahun = int(usia/360)
    hari_sisa = int(usia - (360 * tahun))

    bulan = int(hari_sisa/30)
    hari = int(hari_sisa - (30 * bulan))
    
    print(tahun,"tahun")
    print(bulan,"bulan")
    print(hari,"hari")

usia = int(input("Usia (Dalam Hari) = "))
myDay(usia)


        

