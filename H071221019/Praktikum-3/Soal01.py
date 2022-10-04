X = int(input("Nilai X = "))
Y = int(input("Nilai Y = "))

for i in range(1,Y+1):
    if i % X == 0:
        print(i, end= "\n")
    else: 
        print(i, end= " ")
