print('Program yang mencari duplikat dari 2 buah array')
print('-----------------------------------------------')

a = input("Input Array ke 1: ").split()
b = input("Input Array ke 2: ").split()
set_a = set(a)
set_b = set(b)

tup_a = tuple(set_a & set_b)
print(f'Terdapat {len(set_a & set_b)} buah duplikat yaitu {tup_a}')