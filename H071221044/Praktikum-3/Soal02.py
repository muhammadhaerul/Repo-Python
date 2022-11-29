#2. Cetak elemen pertama hingga n elemen dalam A

n = int(input())
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(3, n+1):
    print(a, end=" ")
    c = a + b
    a = b
    b = c