a = int(input())
b = int(input())

def mencari_FPB (a,b):
    if a > b:
        bilangan_terbesar = a
    else:
        bilangan_terbesar = b

    for i in range (1, bilangan_terbesar + 1):
        if (a % i == 0) and (b % i == 0):
            FPB = i
    return FPB
  
print(f"FPB ({a},{b}) = {mencari_FPB(a,b)}")