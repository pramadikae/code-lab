# Variable and String Formatting

## Variable
Variabel adalah tempat untuk menyimpan data. Nama variabel bebas, tapi tidak boleh diawali angka dan tidak boleh mengandung spasi.

```python
nama = "Andi"
umur = 20
```

## String Formatting
String formatting digunakan untuk memasukkan nilai variabel ke dalam string. Ada beberapa cara:

### 1. Menggunakan tanda +
```python
nama = "Andi"
print("Halo, nama saya " + nama)
```

### 2. Menggunakan f-string (disarankan)
```python
umur = 20
print(f"Umur saya {umur} tahun")
```

### 3. Menggunakan format()
```python
print("Nama saya {} dan umur saya {}".format(nama, umur))
```

## Latihan
1. Buat variabel nama dan umur, lalu tampilkan dengan f-string.
2. Tampilkan kalimat: "Halo, saya [nama], umur [umur] tahun."
