detik = int(input("Masukkan Nilai Detik : "))

jam = detik//(60*60)
sisa_detik = detik-((60*60)*jam)
menit = sisa_detik//60
detik = sisa_detik - (60*menit)
print("%02d:%02d:%02d" % (jam, menit, detik))
