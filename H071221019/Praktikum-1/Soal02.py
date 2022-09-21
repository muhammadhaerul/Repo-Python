# Konversi Detik ke Jam, Menit, dan Detik

detik_awal = int(input("Detik : "))

jam = int(detik_awal/3600)
detik_sisa = int(detik_awal - (3600 * jam))

menit = int(detik_sisa/60)
detik_akhir = int(detik_sisa - (60 * menit))

print("%02d:%02d:%02d" % (jam,menit,detik_akhir))

