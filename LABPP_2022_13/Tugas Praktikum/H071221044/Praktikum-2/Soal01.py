#1. Konversi nilai ke huruf

nilai_siswa = float(input("Nilai= "))

if nilai_siswa >= 90:
    print(f'nilai {nilai_siswa} = "A" ')
elif nilai_siswa >= 80:
    print(f'nilai {nilai_siswa} = "B" ')
elif nilai_siswa >= 70:
    print(f'nilai {nilai_siswa} = "C" ')
elif nilai_siswa  >= 60:
    print(f'nilai {nilai_siswa} = "D" ')
elif nilai_siswa >= 40:
    print(f'nilai {nilai_siswa} = "E" ')
elif nilai_siswa < 40 and nilai_siswa > 0:
    print(f'nilai {nilai_siswa} = "F" ')
else:
    print(f"Nilai tidak valid")