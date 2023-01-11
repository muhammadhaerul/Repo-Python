x = int(input(" "))
y = int(input(" "))
       
def cari_FPB(x,y) :
    if x >= y :
        smallest = x
    else :
        smallest = y
    fpb = 0
    for i in range(1, smallest + 1):
        if x % i == 0 and y % i == 0 :
            fpb = i
    return fpb

print(f"FPB {(x,y)} = {cari_FPB(x,y)}")                     