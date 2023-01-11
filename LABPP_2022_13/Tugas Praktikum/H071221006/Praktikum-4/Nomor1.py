#Nomor1

n = int(input(""))

def faktorial(n):
    if n == 0:
        return 1
    elif n >= 0:
        return n*faktorial(n-1)
    else:
        print("Tidak terdefinisi")

print(faktorial(n))
