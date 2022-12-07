#1. Buatlah program yang mengalikan dua buah matriks 2x2

m1 = []
m2 = []

def matriks1():
    for a in range(2):
        mat_a = []
        for b in range(2):
            m_1 = int(input(f'Input nilai matriks pertama index {a+1},{b+1} : '))
            mat_a.append(m_1)
        m1.append(mat_a)
    return m1
    
def matriks2():
    for a in range(2):
        mat_a = []
        for b in range(2):
            m_2 = int(input(f'Input nilai matriks kedua index {a+1},{b+1} : '))
            mat_a.append(m_2)
        m2.append(mat_a)
    return m2

matriks = [[0,0], 
           [0,0]]

def hasilkali():
    matriks[0][0] = (m1[0][0] * m2[0][0]) + (m1[0][1] * m2[1][0])
    matriks[0][1] = (m1[0][0] * m2[0][1]) + (m1[0][1] * m2[1][1])
    matriks[1][0] = (m1[1][0] * m2[0][0]) + (m1[1][1] * m2[1][0])
    matriks[1][1] = (m1[1][0] * m2[0][1]) + (m1[1][1] * m2[1][1])

    print("Hasil perkalian matriks : ")
    print(f'[{(m1[0][0])} {(m1[0][1])}] x [{(m2[0][0])} {(m2[0][1])}] = [{(matriks[0][0])} {(matriks[0][1])}]')
    print(f'[{(m1[1][0])} {(m1[1][1])}]   [{(m2[1][0])} {(m2[1][1])}]   [{(matriks[1][0])} {(matriks[1][1])}]')

    return matriks

matriks1()
matriks2()
hasilkali()