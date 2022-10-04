n = int(input(" "))
d1 = 0
d2 = 1

for i in range (n):
    print(d1,end= " ")
    d3 = d1 + d2
    d1 = d2
    d2 = d3
    

    