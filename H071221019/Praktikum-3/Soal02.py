nilai = int(input("Nilai n yang menyatakan elemen ke-n = "))
n1 = 0
n2 = 1

for i in range(nilai):
    print(n1, end= " ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3