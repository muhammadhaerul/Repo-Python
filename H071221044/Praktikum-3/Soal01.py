#1. Program untuk mencetak angka


x = int(input())
n = int(input())
for i in range(1, n+1):
    print(i, end=" ")
    if (i % x == 0):
     print("\n")

