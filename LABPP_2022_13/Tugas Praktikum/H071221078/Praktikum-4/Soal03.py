lama_hidup = int(input())

def myDay(lama_hidup):
    tahun = lama_hidup // 360
    bulan = (lama_hidup % 360) // 30
    hari = (lama_hidup % 360) % 30

    print(tahun,'tahun')
    print(bulan,'bulan')
    print(hari,'hari')
    
myDay(lama_hidup)