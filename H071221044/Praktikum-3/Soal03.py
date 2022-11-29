#3. Menghitung kembalian dari suatu transaksi

harga = int(input())
bayar = int(input())
change = bayar - harga
change100 = change // 100000
change50 = (change % 100000) // 50000
change20 = ((change % 100000) % 50000) // 20000
change10 = (((change % 100000) % 50000) % 20000) // 10000
change5 = ((((change % 100000) % 50000) % 20000) % 10000) // 5000
change2 = (((((change % 100000) % 50000) % 20000) % 10000) % 5000) // 2000
change1 = ((((((change % 100000) % 50000) % 20000) % 10000) % 5000) % 2000) // 1000
print(f"{change100} uang Rp. 100.000")
print(f"{change50} uang Rp. 50.000")
print(f"{change20} uang Rp. 20.000")
print(f"{change10} uang Rp. 10.000")
print(f"{change5} uang Rp. 5.000")
print(f"{change2} uang Rp. 2.000")
print(f"{change1} uang Rp. 1.000")
