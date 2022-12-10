import re

kalimat = []
emails = []

# input kalimat
n = int(input())
for i in range(n):
    kalimat.append(input())

# mencari semua alamat email dalam kalimat
for kal in kalimat:
    emails += re.findall(r'[\w\.-]+@[\w\.-]+', kal)

# menampilkan hasil
print(";".join(emails))