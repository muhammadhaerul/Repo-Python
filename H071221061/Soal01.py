import math

h = float(input("masukan ketinggian menara : "))
a = float(input("masukan elevansi ujung belakng kapal : "))
b = float(input("masukan elevansi ujung depan kapal : "))

a1 = math.radians (a)
a2 = math.tan (a1)
a3 = a2 * h
b1 = math.radians (b)
b2 = math.tan(b1)
b3 = b2 * h
c1 = a3 - b3

print(round (c1,1))
