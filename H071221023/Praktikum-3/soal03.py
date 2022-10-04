harga= int(input(" "))
nilaiuang = int(input(" "))
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = nilaiuang - harga
    
if nilaiuang >= harga :
    for i in pecahan :
        jumlah_pecahan = kembalian//i
        kembalian = kembalian - (i*jumlah_pecahan)
        print(f"{jumlah_pecahan} uang Rp. {i:,}".replace(",","."))
    
else :
    print ("Uang Anda tidak cukup")    
    