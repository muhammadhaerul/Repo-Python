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

# def hitung_fpb(a,b):
#     if a > b:
#         terkecil = a
#     else:
#         terkecil = b
#     for i in range(1, terkecil+1):
#         if (a % i == 0) and (b % i == 0):
#             fpb = i
#     return fpb
# print(f"FPB {(a,b)} = ",hitung_fpb(a,b))


def hitung_fpb(a,b):
    while(b):
        a,b = b, a%b
    return a
print(f"FPB {(a,b)} = ", hitung_fpb(a,b))

