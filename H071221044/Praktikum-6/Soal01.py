#1. Buatlah sebuah program untuk menyalin file dengan extensi .txt
nama_file = input("Masukkan nama file: ")+'.txt' 
salinan   = input("Masukkan nama file salinan: ") + ".txt"
baris = int(input("Baris tambahan: "))
try:
  with open(nama_file, "r") as file: 
    baca = file.read() 
  for i in range (baris) :
    b = i + 3
    baca += f"Baris{b}\n"
  with open(salinan,'w') as copy :
    copy.write(baca)
  print('\nBerhasil')

except:
  print('\nGagal')