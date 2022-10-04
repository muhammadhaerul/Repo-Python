#Nomor2

a = int(input(""))

deret1 = 0
deret2 = 1

for i in range(a):
    print(deret1, end=" ")
    rumus_fibonacci = deret1 + deret2
    deret1 = deret2
    deret2 = rumus_fibonacci

