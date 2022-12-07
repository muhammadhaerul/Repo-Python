import re
def buatdata():
    data = {"Nama    "  : input("Silahkan Masukkan Nama Anda : "),
            "Email   "  : "",
            "Password"  : ""}           
    cekEmail = 0
    while cekEmail == 0:
        data["Email   "] = input("Silahkan Masukkan Email Anda : ")
        x = "^[a-z0-9]{1,}@student.unhas.ac.id$"
        if re.search(x, data["Email   "]):
            cekEmail = 1
        else:
            print("=" * 50)
            print("Email yang Anda Masukkan Salah")
            print("=" * 50)
    cekPass = 0
    while cekPass == 0:
        data["Password"] = input("Silahkan Masukkan Password Anda : ")
        y = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$"
        if len(data["Password"]) >= 8: 
            if re.search(y, data["Password"]):
                cekPass = 1
            else:
                print("=" * 50)
                print("Password yang Anda Masukkan Terlalu Lemah")
                print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
                print("=" * 50)
        else:
            print("=" * 50)
            print("Password Harus Memiliki Panjang 8-20 Karakter")
            print("=" * 50)
    return data

def jumlahdata():
    namafile = input("Silahkan Masukkan Nama File : ")
    x = "@student.unhas.ac.id"
    try:
        with open(f"{namafile}.txt", "r") as item:
            jumlah = re.findall(x, item.read())
        print("Berhasil")
        print(f"Jumlah Data Pada File : {jumlah.count(x)} Data")
    except FileNotFoundError:
        print(f"Tidak Terdapat File dengan Nama {namafile}.txt")
        print(f"Jumlah Data Pada File : 0 Data")

def savedata():
    file = input("Silahkan Masukkan Nama File : ")
    try:
        with open(f"{file}.txt", "r") as item:
            item.read()
    except:   
        with open(f"{file}.txt", "w") as item:
            item.write("+" + "="*50 + "\n")
            item.write("|Data yang Tersimpan\n")
            item.write("+" + "="*50 + "\n")
    with open(f"{file}.txt", "a") as save:
        for key,value in data.items():
            save.write(f"|{key} : {value}\n")
        save.write("+" + "="*50 + "\n")
    print("Berhasil")

data = None
while True:
    print("=" * 50)
    print("Selamat Datang Silahkan Pilih Opsi Menu Anda")   
    print(" 1. Detail Anda\n 2. Ubah Nama\n 3. Jumlah Data pada File")
    print(" 4. Save Data Pada File\n 5. Buat Data Baru\n 6. Keluar")
    userinput = int(input("Silahkan Pilih Opsi Anda : "))
    print("=" * 50)
    match userinput:
        case 1:
            if data == None:
                print("> Data Saat Ini Kosong")
            else:
                print("Data Anda Adalah")
                for key,value in data.items():
                    print(f"{key} : {value}")
        case 2:
            if data == None:
                print("> Data Saat Ini Kosong")
            else:
                data["Nama    "] = input("Silahkan Masukkan Nama Baru Anda : ")
                print("Berhasil")
        case 3:
            jumlahdata()
        case 4:
            if data == None:
                print("> Data Saat Ini Kosong")
            else:
                savedata()
                data = None
        case 5:
            data = buatdata()
        case 6:
            print("> Sampai Jumpa Lagi")
            print("=" * 50)
            break
