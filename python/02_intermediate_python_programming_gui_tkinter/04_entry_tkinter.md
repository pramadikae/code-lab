# Membuat Bidang Input di Tkinter

## Penjelasan
Bidang input (Entry) digunakan untuk menerima input teks dari pengguna. Widget ini sangat berguna untuk membuat form atau aplikasi yang membutuhkan data dari user.

### Cara Membuat Bidang Input
Gunakan `tk.Entry()` untuk membuat bidang input. Anda dapat mengambil nilai yang dimasukkan dengan method `.get()`.

```python
entry = tk.Entry(root)
entry.pack()

# Mengambil nilai
nilai = entry.get()
```

## Contoh Program
Lihat kode pada file `04_entry_tkinter.py` berikut:

```python
import tkinter as tk

def tampilkan_nama():
    nama = entry.get()
    label_hasil.config(text=f"Halo, {nama}!")

root = tk.Tk()
root.title("Contoh Entry Tkinter")

label = tk.Label(root, text="Masukkan nama Anda:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Tampilkan", command=tampilkan_nama)
button.pack(pady=5)

label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=5)

root.mainloop()
```

Program di atas akan menampilkan bidang input. Ketika tombol diklik, nama yang dimasukkan akan ditampilkan di label bawahnya.
