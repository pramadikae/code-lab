# Conditional Statement 2 (If, Elif, Else)

Selain `if` dan `else`, Python juga menyediakan `elif` (else if) untuk membuat percabangan lebih dari dua kondisi.

## Struktur Dasar
```python
if kondisi1:
    # kode jika kondisi1 True
elif kondisi2:
    # kode jika kondisi2 True
else:
    # kode jika semua kondisi False
```

## Contoh Penggunaan
```python
nilai = 80
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")
```

## Latihan
1. Buat program yang menampilkan kategori usia: Balita (<5), Anak-anak (5-12), Remaja (13-17), Dewasa (>=18).
2. Modifikasi contoh di atas untuk menambah satu kategori lagi.
