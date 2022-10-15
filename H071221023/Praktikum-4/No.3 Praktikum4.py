umur = int(input(" "))

def MyDay(umur) :
    tahun = int(umur / 360)
    sisa_hari = int(umur - (tahun*360))
    
    bulan = int(sisa_hari / 30)
    hari = int(sisa_hari - (bulan*30))
    
    print(tahun, "Tahun")
    print(bulan, "Bulan")
    print(hari, "Hari")

MyDay(umur)

  
