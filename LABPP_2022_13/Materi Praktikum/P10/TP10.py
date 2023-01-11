import re
import os

def menu():
    print("="*50)
    print(f"Selamat Datang Silahkan Pilih Opsi Menu Anda")
    print(" 1. Detail Anda \n 2. Ubah Nama \n 3. Jumlah Data pada File \n 4. Save Data pada File \n 5. Buat Data Baru \n 6. Keluar")

def buatData():
    data = {
        "Nama": None,
        "Email": None,
        "Password": None
    }
    data["Nama"] = input("Silahkan Masukkan Nama Anda : ")
    while True :
        data["Email"] = input("Silahkan Masukkan Email Anda : ")

        if not re.findall("^[a-z0-9]{1,}(@student\.unhas\.ac\.id$)", data["Email"]):
            print("="*50)
            print("Email yang anda masukkan salah")
            print("="*50)
        else:
            break
    
    while True:
        data["Password"] = input("Silahkan Masukkan Password Anda : ")

        if not (re.fullmatch(".{8,20}", data["Password"])):
            print("="*50)
            print("Password Harus Memiliki Panjang 8-20")
            print("="*50)
        elif not (re.findall("([A-Z]+)", data["Password"]) and re.findall("([a-z]+)", data["Password"]) and re.findall("([0-9]+)", data["Password"])):
            print("="*50)
            print("Password Yang anda masukkan terlalu lemah")
            print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
            print("="*50)
        else:
            break
            
    return data

def simpanData (nama, email, pswd):
    file_name = (input("Silahkan Masukkan Nama File : ") + ".txt")
    
    if os.path.exists(file_name):
        with open(file_name, "a") as file:
            file.write(f"\n|Nama\t\t: {nama}\n")
            file.write(f"|Email\t\t: {email}\n")
            file.write(f"|Password\t: {pswd}\n")
            file.write("+" + "="*100)
        print("Berhasil")
    else:
        with open(file_name, "x") as file:
            file.write("+" + "="*100)
            file.write("\n|Data yang Tersimpan\n")
            file.write("+" + "="*100)
            file.write(f"\n|Nama\t\t: {nama}\n")
            file.write(f"|Email\t\t: {email}\n")
            file.write(f"|Password\t: {pswd}\n")
            file.write("+" + "="*100)
        print("Berhasil")

def jumlahData ():
    file_name = (input("Silahkan Masukkan Nama File : ") + ".txt")
    
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data_count = (len(file.readlines()) - 3) / 4
        print("Berhasil")
        return int(data_count)
    else:
        print(f"Tidak Terdapat File dengan nama {file_name}")
        return 0
        
# ========================================================================================== #
# ========================================================================================== #

data = None
while True:    
    menu() #function untuk tampilkan menu
    opsi = int(input(" Silahkan Pilih Opsi Anda : ")) #input
    print("="*50)
    match opsi:
        case 1:
            if data == None:
                print ("Data Saat Ini Kosong")
            else:
                print("Data anda adalah")
                print(f"Nama : {data['Nama']}")
                print(f"Umur : {data['Email']}")
                print(f"Alamat : {data['Password']}")
        case 2:
            if data == None:
                print ("Data Saat Ini Kosong")
            else:
                data["Nama"] = input("Silahkan Input Nama Baru : ")
        case 3:
            jumlah_data = jumlahData() #function yang kedua untuk menampilkan jumlah data
            print(f"Jumlah Data Pada File : {jumlah_data} Data")
        case 4:
            if data == None:
                print ("Data Saat Ini Kosong")
            else:
                simpanData(data["Nama"],data["Email"],data["Password"])
                data = None
        case 5:
            data = buatData()
        case 6:
            print(f"Sampai Jumpa Lagi")
            break
    