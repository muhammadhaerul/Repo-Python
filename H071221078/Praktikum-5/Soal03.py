x = set(map(int, input('Input array ke 1: ').split()))
y = set(map(int, input('Input array ke 2: ').split()))

i = x.intersection(y)
i = tuple(i)
if len(i) == 0:
    print('Tidak terdapat duplikat')
else:    
    print(f'Terdapat {len(i)} buah duplikat yaitu {i}')