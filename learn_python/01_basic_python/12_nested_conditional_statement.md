# Nested Conditional Statement

Nested conditional statement adalah percabangan yang berada di dalam percabangan lain. Ini berguna jika Anda ingin memeriksa beberapa kondisi secara bertingkat.

## Contoh Penggunaan
```python
umur = 20
if umur >= 18:
    if umur < 65:
        print("Dewasa")
    else:
        print("Lansia")
else:
    print("Anak-anak atau Remaja")
```

## Latihan
1. Buat program yang memeriksa apakah sebuah angka positif, negatif, atau nol, lalu jika positif cek apakah genap atau ganjil.
2. Modifikasi contoh di atas untuk menambah kategori usia.
