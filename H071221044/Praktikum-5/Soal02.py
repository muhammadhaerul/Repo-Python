#2. Buat program untuk mengubah detail data anda

print("Selamat datang! untuk memulai silahkan input data Anda")
Nama = input("Input nama : ")
Umur = int(input("Input umur : "))
Alamat = input("Input alamat : ")

dict_data = {
    "nama" : Nama, 
    "umur" : Umur, 
    "alamat" : Alamat
    }

while True :
    print("="*50)
    print(f"Halo {dict_data['nama']} silahkan pilih opsi")
    print("="*50)
    print("1. Detail anda")
    print("2. Ubah nama")
    print("3. Ubah umur")
    print("4. Ubah alamat")
    print("5. Keluar")
    print("="*50)

    
    opsi = int(input("Input opsi : "))

    print("="*50)

    if opsi == 1 :
        print("Data anda adalah : ")
        print(f"Nama : {dict_data['nama']}")
        print(f"Umur : {dict_data['umur']}")
        print(f"Alamat : {dict_data['alamat']}")
    elif opsi == 2 :
        ubah_nama = input("Silahkan input nama baru : ")
        dict_data['nama'] = ubah_nama
        print("Data anda sukses diperbarui")
    elif opsi == 3 :
        ubah_umur = int(input("Silahkan input umur baru : "))
        dict_data['umur'] = ubah_umur
        print("Data anda sukses diperbarui")
    elif opsi == 4 :
        ubah_alamat = input("Silahkan input alamat baru : ")
        dict_data['alamat'] = ubah_alamat
        print("Data anda sukses diperbarui")
    elif opsi == 5 :
        print(f"Selamat tinggal {dict_data['nama']}")
        break