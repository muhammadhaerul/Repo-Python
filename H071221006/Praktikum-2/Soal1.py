#Nomor1

print("Konversi nilai dalam bentuk angka ke huruf")

nilai = float(input("Nilai: "))

if nilai >= 90:
    huruf = "'A'"
elif nilai >= 80:
    huruf = "'B'"
elif nilai >= 70:
    huruf = "'C'"
elif nilai >= 60:
    huruf = "'D'"
elif nilai >= 40:
    huruf = "'E'" 
else:
    huruf = "'F'"
print('Nilai', nilai, '=', huruf)

