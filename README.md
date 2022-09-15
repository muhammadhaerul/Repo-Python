# Repositori Tugas Praktikum Pengantar Pemrograman 2022

## Alur pengumpulan tugas ke repositori ini

1. **Fork** repositori ini

2. **Clone** repositori hasil **fork** anda

   ```sh

   git clone https://github.com/YOUR_USERNAME/LABPP_2022_13.git

   ```

3. Setelah anda **clone**, masuk ke folder hasil **clone** tersebut lalu buat **branch** dengan nama **NIM** anda

   ```sh

   cd LABPP_2022_5
   git branch NIM_ANDA
   git checkout NIM_ANDA
   git config user.name USERNAME_GITHUB
   git config user.email EMAIL_GITHUB

   ```

4. Setelah anda pindah ke **branch** yang telah anda buat, buat sebuah folder dengan nama **NIM** anda dan masuk ke folder tersebut.
   ```sh

   mkdir NIM_ANDA
   cd NIM_ANDA

   ```


5. Didalam folder tersebut, buat sebuah folder dengan nama **Praktikum-n**, **n** = praktikum keberapa
   ```sh

   mkdir "Praktikum-n"
   cd "Praktikum n"

   ```

7. Semua _file_ untuk tugas praktikum ke-**n**, disimpan kedalam folder **Praktikum n**
8. Setiap membuat _file_ atau melakukan perubahan, lakukan proses **commit** dengan pesan yang deskriptif

   ```sh
   git add . #perintah ini memilih seluruh file sekaligus
   # atau
   git add "Praktikum n/NIM/FilePythonYangBerubahAtauDitambahkan.py" #perintah ini memilih file tertentu
   git commit -m "pesan mengenai penambahan atau perubahan apa yang anda lakukan"
   
   ```

8. Setelah asistensi dan tugas anda disetujui, **push** seluruh _file_ jawaban yang telah anda buat

   ```sh

   # pastikan proses commit telah selesai terhadap setiap file
   git push origin NIM_ANDA

   ```
   
9. 

## Hal-hal yang harus diperhatikan

- [x] Cara mengumpulkan tugas sesuai dengan aturan diatas.
- [x] _**Satu Praktikum, Satu Folder**_.
- [x] _**Satu Soal, Satu Class**_.
- [x] _**Program Berjalan dengan Baik dan Benar Berdasarkan Ketentuan Tugas**_.
