n = int(input('Masukan Detik : '))

jam = n // 3600
sisa = n % 3600
menit = sisa // 60
detik = sisa % 60


print(f"j:m:d => {jam}:{menit}:{detik}")
print("%02d:%02d:%02d" % (jam,menit,detik))
