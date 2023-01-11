# Repositori Tugas Praktikum Lab Pengantar Pemrograman 2022

## Requirements:
1. Buat akun GitHub (https://github.com/)
2. Download Git (https://git-scm.com/)


## Alur pengumpulan tugas ke repositori ini:

1.  **Fork** repositori ini menggunakan akun GitHub anda

2. Buka Git Bash dan **clone** repositori hasil **fork** anda

   ```sh

   git clone https://github.com/YOUR_USERNAME/LABPP_2022_13.git

   ```

3. Setelah anda **clone**, masuk ke folder hasil **clone** tersebut dan lakukan config.

   ```sh
   
   cd LABPP_2022_5

   git config user.name USERNAME_GITHUB
   git config user.email EMAIL_GITHUB

   ```

4. Buat **branch** baru dengan nama **NIM**, dan lakukan **checkout** untuk berpindah dari **main branch** ke **branch** tersebut.
   ```sh
   
   git branch NIM_ANDA
   git checkout NIM_ANDA
   
   ```

5. Buat sebuah folder dengan nama **NIM** anda dan masuk ke folder tersebut.
   ```sh

   mkdir NIM_ANDA
   cd NIM_ANDA

   ```


6. Didalam folder tersebut, buat sebuah folder dengan nama **Praktikum-n**, **n** = praktikum ke-berapa. 
   ```sh

   mkdir "Praktikum-n"
   cd "Praktikum-n"

   ```
   Semua _file_ untuk tugas praktikum ke-**n**, disimpan kedalam folder **Praktikum-n** dengan nama _file_ **Soal01.py**, **Soal02.py**, dst.

7. Tambahkan _file_ tugas-tugas praktikum anda, liat perubahan yang terjadi, dan lakukan proses **commit** dengan pesan yang deskriptif.

   ```sh
   
   #tambahkan file
   git add . #perintah ini memilih seluruh file sekaligus
   #atau
   git add "File_python_yang_berubah_atau_ditambahkan.py" #perintah ini memilih file tertentu
   
   #liat perubahan
   git status
   
   #lakukan commit
   git commit -m "pesan mengenai penambahan atau perubahan apa yang anda lakukan"
   
   ```

8. Setelah asistensi dan tugas praktikum anda disetujui oleh asisten, **push** seluruh _file_ jawaban yang telah anda buat.
   Pastikan proses commit telah selesai terhadap setiap file sebelum melakukan **push**
   
   ```sh
   
   #push tugas
   git push

   ```
   
   Jika sebelumnya anda belum pernah menghubungkan Git di komputer anda dengan akun GitHub anda, maka anda akan diminta untuk mengisi username dan password untuk
   melakukan push ke repo GitHub anda.
   ```sh

   # username = username anda
   # password = persocal access token anda

   ```
   
   Cara membuat personal access token:
   ```sh
   
   #1. Klik profile anda pada pojok kanan atas GitHub
   #2. Pilih menu settings
   #3. Scroll ke bagian bawah dan pilih menu Dveloper settings
   #4. Pilih Prsonal access tokens
   #5. Pilih Generate new tokes
   #6. Tuliskan note untuk token anda (ex: Token for LABPP_2022_13)
   #7. Atur waktu expiration token anda (sesuai keinginan anda)
   #8. Pada select scope, ceklis box repo
   #9. Klik generate new token
   #10. Pastikan untuk meng-copy token anda dan menyimpannya, karena token hanya bisa diliat sekali (*Jika hilang, buat token baru)

   ```
   
9. Masuk ke akun GitHub anda, dan buka repo yang telah anda **fork** dan **clone**. Lihat perubahan yang terjadi pada repo tersebut dan pastikan bahwa tugas yang
   telah anda **push** sesuai dan berada pada repo tersebut.
   
10. Pilih menu **Pull request** dan lakukan **pull request** pada tugas praktikum anda.


## Hal-hal yang harus diperhatikan:
- [x] Cara mengumpulkan tugas sesuai dengan aturan diatas.
- [x] _**Satu Praktikum, Satu Folder**_.
- [x] _**Satu Soal, Satu File**_.
- [x] _**Program Berjalan dengan Baik dan Benar Berdasarkan Ketentuan Tugas**_.
