#3. Buatlah program yang mencari duplikat dari 2 buah array

array1=list(map(int,input("Input array ke 1: ").split(" ")))
array2= list(map(int,input("Input array ke 2: ").split(" ")))
irisan=[]
for i in array2:
    if i in array1 :
        irisan.append(i)
arrays= tuple(irisan)
print(f"Terdapat {len(irisan)} buah duplikat yaitu {arrays}")

#map untuk mengubah fungsi jadi l
# #split misahn string