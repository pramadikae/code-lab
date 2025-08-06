# Logical Operators

Operator logika digunakan untuk menggabungkan dua atau lebih kondisi. Operator logika di Python:

- `and`: True jika kedua kondisi True
- `or`: True jika salah satu kondisi True
- `not`: Membalik nilai boolean

## Contoh Penggunaan
```python
umur = 25
lulus = True
print(umur > 18 and lulus)  # True
print(umur < 18 or lulus)   # True
print(not lulus)            # False
```

## Latihan
1. Buat dua variabel boolean, lalu coba kombinasi dengan and, or, dan not.
2. Buat kondisi: jika umur di atas 17 dan sudah lulus, tampilkan "Bisa daftar kuliah".
