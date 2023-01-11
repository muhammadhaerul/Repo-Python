matriks1 = []
matriks2 = []
matriks3 = []

for i in range(2):
    matriks1.append([])
    for j in range(2):
        baru = int(input(f'Input nilai matriks pertama index {i+1},{j+1}: ' ))
        matriks1[i].append(baru)

for i in range(2):
    matriks2.append([])
    for j in range(2):
        baru = int(input(f'Input nilai matriks kedua index {i+1},{j+1}: ' ))
        matriks2[i].append(baru)

for i in range(len(matriks1)):
    baris = []
    for j in range(len(matriks1[0])):
        total = 0
        for k in range(len(matriks1)):
            total += matriks1[i][k]*matriks2[k][j]
        baris.append(total)
    matriks3.append(baris)

print('Hasil perkalian matriks')
print(f'| {matriks1[0][0]}, {matriks1[0][1]} | x | {matriks2[0][0]}, {matriks2[1][0]} | = | {matriks3[0][0]}, {matriks3[0][1]} |')
print(f'| {matriks1[1][0]}, {matriks1[1][1]} | x | {matriks2[1][0]}, {matriks2[1][1]} |   | {matriks3[1][0]}, {matriks3[1][1]} |')

