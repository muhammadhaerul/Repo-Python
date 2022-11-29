m1= []  
for i in range(2):
    m1.append([])
    for j in range(2):
        a = int(input(f"Input nilai matriks pertama index {i + 1},{j + 1}: "))
        m1[i].append(a)
m2= []  
for i in range(2):
    m2.append([])
    for j in range(2):
        b = int(input(f"Input nilai matriks kedua index {i + 1},{j + 1}: "))
        m2[i].append(b)
m_hasil=[]
for i in range(2):
    m_hasil.append([])
    for j in range(2):
        x = (m1[i][0] * m2[0][j]) + (m1[i][1] * m2[1][j])
        m_hasil[i].append(x)

#m_hasil = [[0 for i in range(2)] for j in range(2)]
#for i in range(2):
#    for j in range(2):
#        m_hasil[i][j] = (m1[i][0] * m2[0][j]) + (m1[i][1] * m2[1][j])

print("Hasil Perkalian Matriks:")
print(f'{m1[0]} x {m2[0]} =',m_hasil[0])
print(f'{m1[1]}   {m2[1]}  ',m_hasil[1])