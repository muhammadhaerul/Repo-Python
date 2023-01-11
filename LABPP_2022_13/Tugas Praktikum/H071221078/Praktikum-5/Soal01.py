matriks1 = []
for i in range(1,3):
    for j in range(1,3):
        a = int(input(f'Input nilai matriks pertama indeks {i},{j}: '))
        matriks1.append(a)

matriks2 = []
for m in range(1,3):
    for n in range(1,3):
        b = int(input(f'Input nilai matriks kedua indeks {m},{n}: '))
        matriks2.append(b)

p = matriks1[0]*matriks2[0] + matriks1[1]*matriks2[2]
q = matriks1[0]*matriks2[1] + matriks1[1]*matriks2[3]
r = matriks1[2]*matriks2[0] + matriks1[3]*matriks2[2]
s = matriks1[2]*matriks2[1] + matriks1[3]*matriks2[3]

print('Hasil perkalian matriks')
print(f'|{matriks1[0]} {matriks1[1]}| X |{matriks2[0]} {matriks2[1]}| = |{p} {q}|')
print(f'|{matriks1[2]} {matriks1[3]}|   |{matriks2[2]} {matriks2[3]}|   |{r} {s}|')