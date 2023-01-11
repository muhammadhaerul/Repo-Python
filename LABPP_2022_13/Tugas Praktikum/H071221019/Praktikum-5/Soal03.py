array1 = set(map(int, input("Input array ke 1: ").split()))
array2 = set(map(int, input("Input array ke 2: ").split()))

duplikat = array1.intersection(array2)
duplikat = tuple(duplikat)

if len(duplikat) == 0:
    print("> Tidak ada Duplikat")
else:
    print("> Terdapat",len(duplikat),"buah duplikat yaitu",duplikat)