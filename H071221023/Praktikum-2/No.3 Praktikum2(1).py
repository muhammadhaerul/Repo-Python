a = int (input ("a = "))
b = int (input ("b = "))
c = int (input ("c = "))

if  a >= b and a >= c :
    terbesar = a
elif b >= a and b >= c :
    terbesar = b
else :
    terbesar = c

print (terbesar, "adalah nilai terbesar")