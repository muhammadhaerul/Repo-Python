#1. Buatlah sebuah program yang jika dijalankan akan menampilkan menu seperti di soal:
import re
print('='*100)


# nama = input('Nama : ')
# email = input('Email : ')
# password = input('Password : ')

data = {"Nama" : None , "Email" : None, "Password" : None}

while True :
    print("="*100)
    print(f"Halo! silahkan pilih opsi : ")
    print("="*100)
    print("1. Detail anda")
    print("2. Ubah nama")
    print("3. Jumlah data pada file")
    print("4. Save data pada file")
    print("5. Buat data baru")
    print("6. Keluar")
    print("="*100)

    opsi = int(input("Opsi yang diinginkan : "))

    if opsi == 1 :
        if data == None :
            print("Data saat ini kosong : ")
        else :
            print("Data anda adalah : ")
            print(f"Nama : {data['Nama']}")
            print(f"Email : {data['Email']}")
            print(f"Password : {data['Password']}")

    elif opsi == 2 :
        if data == None :
            print("Data saat ini kosong : ")
        else :
            ubah_nama = input("Silahkan input nama baru : ")
            data['nama'] = ubah_nama

    elif opsi == 3 :
        pass
    elif opsi == 4 :
        pass
    elif opsi == 5 :
    
            data['nama'] = input("Silahkan input nama : ")
            pola = "[a-zA-Z0-9]+@student.unhas.ac.id"
            while True :
                email= input ("silahkan input email: ")
                hasil = re.match(pola, email)
            
                if hasil == None :
                    print ("email yang anda masukkan salah")
                else :
                    data['email'] = input("Silahkan input email : ")
                    break

            # data['password'] = input("Silahkan input password : ")

    elif opsi == 6 :
        pass