print("=" * 50)
print("Selamat Datang")
print("Untuk Memulai Silahkan Input Data Anda")
print("=" * 50)
data = {"Nama":input("Input Nama: "),
        "Umur":input("Input Umur: "),
        "Alamat":input("Input Alamat: ")}
n = 0
while n == 0:
    print("=" * 50)
    print(f"     Selamat Datang {data['Nama']} Silahkan Pilih Opsi")
    print("=" * 50)
    print("1. Detail Anda \n2. Ubah Nama \n3. Ubah Umur \n4. Ubah Alamat \n5. Keluar")
    print("=" * 50)
    userinput = int(input("> Input Opsi: "))
    print("=" * 50)
    if userinput == 1:
        print("Data Anda Adalah")
        for key,value in data.items():
            print(f"{key}: {value}")
    elif userinput == 2:
        data["Nama"] = input("Silahkan input nama baru: ")
        print("Data Anda Sukses Diperbarui")
    elif userinput == 3:
        data["Umur"] = input("Silahkan input umur baru: ")
        print("Data Anda Sukses Diperbarui")
    elif userinput == 4:
        data["Alamat"] = input("Silahkan input alamat baru: ")
        print("Data Anda Sukses Diperbarui")
    elif userinput == 5:
        print(f"            Selamat Tinggal {data['Nama']} :)")
        print("=" * 50)
        nilai = 1
        break