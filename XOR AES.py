"""
AES MixColumns Verbose Helper
-----------------------------

Kode ini dibuat sebagai alat bantu pribadi untuk memahami dan menghitung langkah MixColumns dalam algoritma AES secara manual. 

"""

def gmul(a, b):
    """Perkalian di GF(2^8) dengan modulus 0x11b (digunakan dalam AES MixColumns)"""
    p = 0  # Hasil akhir
    for i in range(8):  # Lakukan 8 kali (karena 1 byte = 8 bit)
        if b & 1:
            p ^= a  # Jika bit LSB dari b = 1, tambahkan a ke hasil (XOR)
        hi_bit_set = a & 0x80  # Cek apakah bit tertinggi dari a = 1
        a = (a << 1) & 0xFF  # Kalikan a dengan x (shift kiri 1 bit)
        if hi_bit_set:
            a ^= 0x1b  # Jika bit tertinggi tadinya 1, lakukan modulo dengan x^8 + x^4 + x^3 + x + 1 (0x11b)
        b >>= 1  # Geser b ke kanan
    return p

def bin_str(x):
    """Format biner 8-bit dari angka"""
    return format(x, '08b')

def mix_single_column(col, col_index=0):
    """
    Melakukan transformasi MixColumns pada satu kolom state AES.
    Argumen:
    - col: daftar 4 byte (satu kolom)
    - col_index: indeks kolom (untuk keperluan print)
    """
    # Matriks konstan MixColumns AES
    mix = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ]
    result = [0] * 4  # Hasil akhir kolom

    print(f"\n--- Kolom {col_index + 1} ---")
    print(f"Input: {[hex(c) for c in col]}")

    for i in range(4):  # Untuk setiap baris dalam kolom hasil
        temp = []
        print(f"\n  Baris {i + 1}:")
        for j in range(4):  # Kombinasikan setiap elemen dengan konstanta dari matriks mix
            m = mix[i][j]
            val = gmul(m, col[j])
            temp.append(val)
            print(f"    gmul({m}, {hex(col[j])}) = {hex(val)} ({bin_str(val)})")
        result[i] = temp[0] ^ temp[1] ^ temp[2] ^ temp[3]
        print(f"    XOR result: {hex(temp[0])} ^ {hex(temp[1])} ^ {hex(temp[2])} ^ {hex(temp[3])} = {hex(result[i])}")
        print(f"    Binary XOR result: {bin_str(temp[0])} ^ {bin_str(temp[1])} ^ {bin_str(temp[2])} ^ {bin_str(temp[3])} = {bin_str(result[i])}")
    return result

def mix_columns_verbose(state):
    """
    Menerapkan MixColumns ke seluruh state (4x4 byte array).
    Menampilkan langkah-langkah perhitungan untuk tiap kolom.
    """
    for c in range(4):  # Untuk setiap kolom
        col = [state[r][c] for r in range(4)]  # Ambil kolom sebagai list
        mixed = mix_single_column(col, col_index=c)
        for r in range(4):  # Simpan hasilnya ke state
            state[r][c] = mixed[r]
    return state

# Input contoh (berdasarkan contoh gambar/soal)
example_state = [
    [0x4e, 0xfd, 0xf5, 0xc5],
    [0xf2, 0xc6, 0x7a, 0xe5],
    [0x5d, 0x41, 0x9d, 0x6b],
    [0xe7, 0xfb, 0xf8, 0xe1]
]

print("=== Proses MixColumns AES dengan Detail (Input dari gambar) ===")
mixed_state = mix_columns_verbose(example_state)

print("\n=== Hasil Akhir State Setelah MixColumns ===")
for row in mixed_state:
    print(['{:02x}'.format(b) for b in row])
