def getFPB(a, b):
    if a >= b:
        c = a
    else:
        c = b
    fpb = 0
    for i in range(1, c+1):
        if a % i == 0 and b % i == 0:
            fpb = i            
    return fpb

a = int(input("Angka 1 = "))
b = int(input("Angka 2 = "))
print(f"FPB ({a},{b}) = {getFPB(a, b)}")