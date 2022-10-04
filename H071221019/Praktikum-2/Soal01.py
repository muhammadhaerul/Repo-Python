# Program mengkonversikan nilai dalam bentuk angka ke huruf

nilai = float(input("Nilai = "))

if nilai >= 90:
    print("> Nilai",nilai, "= A")
elif nilai >= 80:
    print("> Nilai",nilai, "= B")
elif nilai >= 70:
    print("> Nilai",nilai, "= C")
elif nilai >= 60:
    print("> Nilai",nilai, "= D")
elif nilai >= 40:
    print("> Nilai",nilai, "= E")
else:
    print("> Nilai",nilai, "= F")