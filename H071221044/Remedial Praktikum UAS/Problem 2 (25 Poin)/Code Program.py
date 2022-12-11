pesan = input()

# menghapus karakter $
clean_pesan = pesan.replace("$", "")

# balik pesan
balik_pesan = clean_pesan[::-1]

# menampilkan hasil
print(balik_pesan)