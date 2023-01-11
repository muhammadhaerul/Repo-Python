import os
import re

data = {
    'nama': None,
    'email': None,
    'password': None
}

def resetData(data):
    data['nama'] = None
    data['email'] = None
    data['password'] = None

def saveData():
    file = input('Silahkan masukkan nama file : ') + '.txt'
    if os.path.isfile(file) == False:
        with open(file, 'w') as fl:
            fl.write('+' + '=' * 50)
            fl.write('\n| Data yang tersimpan')
            fl.write('\n+' + '=' * 50)
            fl.write('\n|Nama' + ' ' *12 + ':' + data.get('nama'))
            fl.write('\n|Email' + ' ' *11 + ':' + data.get('email'))
            fl.write('\n|Password' + ' ' *8 + ':' + data.get('password'))
            fl.write('\n+' + '=' * 50)
            resetData(data)
    else:
        with open(file, 'a') as fl:
            fl.write('\n|Nama' + ' ' *12 + ':' + data.get('nama'))
            fl.write('\n|Email' + ' ' *11 + ':' + data.get('email'))
            fl.write('\n|Password' + ' ' *8 + ':' + data.get('password'))
            fl.write('\n+' + '=' * 50)
            resetData(data)
    
def ubahData(data):
    while True:
        Email = input('Silahkan Masukkan Email Anda : ')
        if not re.fullmatch(r'[a-z0-9]{1,}@student[.]unhas[.]ac[.]id', Email):
            print('===============================================')
            print('Email yang Anda Masukkan Salah')
            print('===============================================')
        else:
            data['email'] = Email
            break
    while True:
        Password = input('Silahkan Masukkan Password Anda : ')
        if not re.fullmatch(r'[\w\s/*-=+)(*&^%$#@!><,.?~`]{8,20}', Password):
            print('===============================================')
            print('Password harus memiliki panjang 8-20 karakter')
            print('===============================================')
        elif not re.findall(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', Password):
            print('===============================================')
            print('Password yang Anda Masukkan Terlalu Lemah, Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka')
            print('===============================================')
        elif (re.fullmatch(r'[\w\s/*-=+)(*&^%$#@!><,.?~`]{8,20}', Password) and re.findall(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', Password)):
            data['password'] = Password
            break

def hitungData(file):
    if os.path.isfile(file) == True:
        open_file = open(file, 'r')
        banyak_data = open_file.read().lower().count('nama')
        print(f'Berhasil\nJumlah Data Pada File : {banyak_data} Data')
    else:
        print(f'\nTidak Terdapat File dengan Nama {file}')
        print('Jumlah Data Pada File: 0 Data\n')

while True:
    print('====================Menu======================')
    print('1. Detail anda\n2. Ubah nama \n3. Jumlah data pada file \n4. Save data pada file \n5. Buat data baru \n6. Keluar')
    print('===============================================')

    opsi = int(input('Silahkan Pilih Menu Anda : '))
    print('===============================================')

    match opsi:         
        case 2:
            if (data.get('nama') and data.get('email') and data.get('password')) == None:
                print('\nData saat ini kosong\n')
            else:
                data['nama'] = input()

        case 3:
            file = input('Silahkan Masukkan Nama File : ') + '.txt'
            hitungData(file)

        case 4:
            if (data.get('nama') and data.get('email') and data.get('password')) == None:
                print('\nData saat ini kosong\n')
            else:
                saveData() 

        case 5:
            Nama = input('Silahkan Masukkan Nama Anda : ')
            data['nama'] = Nama
            ubahData(data)

        case 1:
            if (data.get('nama') and data.get('email') and data.get('password')) == None:
                print('\nData saat ini kosong\n')
            else:
                print('\nData Anda adalah\nNama :', data.get('nama'), '\nEmail : ', data.get('email'), '\nPassword : ', data.get('password'),'\n')

        case 6:
            print('\nSampai jumpa lagi\n')
            print('===============================================')
            break