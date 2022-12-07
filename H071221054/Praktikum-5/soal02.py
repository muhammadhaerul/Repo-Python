# Program Mengubah Detail Data

def profil():
    print("=" * 60)
    print('Selamat datang', data_dict.get('Nama') ,'silahkan pilih opsi')
    print("=" * 60)

print("=" * 60)
print("Selamat datang untuk memulai silahkan input data anda")
print("=" * 60)

nama = input("Input Nama Anda : ")
umur = int(input("Input Umur Anda : "))
alamat = input("Input Alamat Anda : ")

data_dict = {
"Nama": nama, 
"Umur": umur,
"Alamat": alamat 
}

profil()

while True:
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("=" * 60)
    a = input("Input opsi : ")
    print("=" * 60)

    try :
        a = int(a)
    except :
        print("Inputan salah")
    else:
        match a:
            case 1:
                print("Data anda adalah")
                print('Nama :', data_dict.get('Nama'))
                print('Umur :', data_dict.get('Umur'))
                print('Alamat :', data_dict.get('Alamat'))
                profil()
            case 2:
                nama_baru = input("Silahkan Input nama baru : ")
                data_dict['Nama'] = nama_baru
                print("Data Anda sukses di perbarui")
                profil()
            case 3:
                umur_baru = input("Silahkan input umur baru : ")
                data_dict['Umur'] = umur_baru
                print("Data Anda sukses di perbarui")
                profil()
            case 4:
                alamat_baru = input("Silahkan input alamat baru : ")
                data_dict['Alamat'] = alamat_baru
                print("Data Anda sukses di perbarui")
                profil()
            case 5:
                print('Selamat Tinggal', data_dict.get('Nama'))
                break