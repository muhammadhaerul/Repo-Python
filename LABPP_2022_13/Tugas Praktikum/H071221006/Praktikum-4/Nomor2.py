#Nomor2

print("Menentukan FPB")

while True:
    try:
        a = int(input(''))
        b = int(input(''))
        break
    except:
        print("Input hanya terdiri dari angka")
        continue
        
def hitung_fpb(a,b):
    while(b):
        a,b = b, a%b
    return a
print(f"FPB {(a,b)} = ", hitung_fpb(a,b))

