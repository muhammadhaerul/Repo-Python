file = input()
jumlah = int(input())

nama = []
nim = []
angkatan = []

for i in range(jumlah): #perulangan untuk isi biodata sebanyak jumlah yang kita inginkan
    isi_nama = input('Masukkan Nama: ').replace(' ','_')
    if len(isi_nama) <= 20:
        nama.append(isi_nama)
    else:
        print('Gagal')
        exit()
    isi_nim = input('Masukkan NIM: ')
    nim.append(isi_nim)
    isi_angkatan = input('Masukkan Angkatan: ')
    angkatan.append(isi_angkatan)

if len(isi_nama) <= 20:
    with open(f"{file}.txt","w") as f:
        nama_terpanjang = nama[0]
        for panjang in nama: #mencari nama yang terpanjang
            if len(panjang) > len(nama_terpanjang):
                nama_terpanjang = panjang

        f.write('+-'+('-'*len(nama_terpanjang))+'-+') #baris pertama atau paling atas dari tabel
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        f.write('\n| Nama'+(' '*(len(nama_terpanjang)-5))+'  |') #baris kedua untuk kolom format Nama, NIM, Angkatan
        f.write(' NIM'+(' '*(12-4))+'|')
        f.write(' Angkatan'+(' '*(10-9))+'|')

        f.write('\n+-'+('-'*len(nama_terpanjang))+'-+') #baris ketiga batas antara format dan isi
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        for x in range(jumlah): #baris selanjutnya isi sesuai banyak data yang di input
            f.write('\n| ')
            f.write(nama[x])
            f.write(' '*(len(nama_terpanjang)-len(nama[x]))+' | ')
            f.write(nim[x])
            f.write(' '*(11-len(nim[x]))+'| ')
            f.write(angkatan[x])
            f.write((' '*(9 - len(angkatan[x])))+'|')

        f.write('\n+-'+('-'*len(nama_terpanjang))+'-+') #baris paling akhir sebagai penutup
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        print('Berhasil')


        

