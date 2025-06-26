# AES-MixColumns

Proyek ini adalah **alat bantu pribadi** yang saya buat untuk **mempermudah proses manual MixColumns dalam algoritma AES**.

## Apa itu MixColumns?

MixColumns adalah salah satu langkah dalam algoritma enkripsi AES yang melakukan **difusi** data antar byte dalam kolom. Ini dilakukan dengan perkalian matriks tetap dan operasi di medan hingga (Galois Field 2^8), yang tidak bisa dihitung seperti perkalian biasa.

## Cara Menjalankan

```bash
git clone https://github.com/username/aes-mixcolumns-helper.git
cd aes-mixcolumns-helper
python mix_columns_verbose.py
```
## Contoh Input
```
example_state = [
    [0x4e, 0xfd, 0xf5, 0xc5],
    [0xf2, 0xc6, 0x7a, 0xe5],
    [0x5d, 0x41, 0x9d, 0x6b],
    [0xe7, 0xfb, 0xf8, 0xe1]
]
```
## Contoh Output
![Contoh Output](https://github.com/user-attachments/assets/0f48a6e8-6f07-4323-9388-7c8139956395)
![image](https://github.com/user-attachments/assets/c1c751fe-0a8a-4b2a-8fbb-ba92e85ccbfd)


