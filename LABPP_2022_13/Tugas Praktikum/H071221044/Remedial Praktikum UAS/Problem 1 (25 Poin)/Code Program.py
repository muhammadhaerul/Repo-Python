# input panjang pola x
n = int(input())

# perulangan untuk mencetak pola x
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("x", end="")
        else:
            print("-", end="")
    print()
