print('Program yang mengalikan dua buah matriks 2x2')
print('--------------------------------------------')

def matriks1(label, mat):
    for baris in range(2):
        mat_baris = []
        for kolom in range(2):
            elemen_baru = int(input(f'Input nilai matriks {label} index {baris+1},{kolom+1} : '))
            mat_baris.append(elemen_baru)
        mat.append(mat_baris)
    return mat

hasil = [[0,0],
          [0,0]]

def hasilkali(mat1, mat2):
    for i in range(2):
        for j in range(2):
            for k in range(2): 
                hasil[i][j] += (mat1[i][k] * mat2[k][j])
            
    print(' |',  (mat1[0][0]),(mat1[0][1]), '|', 'x', '|', (mat2[0][0]),(mat2[0][1]), '|', '=', '|', (hasil[0][0]),(hasil[0][1]), '|')
    print(' |',  (mat1[1][0]),(mat1[1][1]), '|', ' ', '|', (mat2[1][0]),(mat2[1][1]), '|', ' ', '|', (hasil[1][0]),(hasil[1][1]), '|')

mat1 = []
mat2 = []
mat1 = matriks1("pertama", mat1)
mat2 = matriks1("kedua", mat2)
hasilkali(mat1, mat2)