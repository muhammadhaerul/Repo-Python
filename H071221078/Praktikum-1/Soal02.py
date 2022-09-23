detik = int(input("Masukkan jumlah detik: "))

jam = int(detik/(3600))
menit = int((detik-(jam*3600))/60)
detik = int(detik-((3600*jam)+(60*menit)))

print(f'{jam:02d} : {menit:02d} : {detik:02d}')

