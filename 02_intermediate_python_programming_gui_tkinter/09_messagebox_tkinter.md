# Kotak Pesan di Tkinter

## Penjelasan
Kotak pesan (messagebox) digunakan untuk menampilkan pesan pop-up seperti informasi, peringatan, atau konfirmasi kepada pengguna. Tkinter menyediakan modul `messagebox` untuk membuat berbagai jenis kotak pesan.

### Cara Menggunakan messagebox
Import modul `messagebox` dari `tkinter`:

```python
from tkinter import messagebox
```

Contoh penggunaan:
- `messagebox.showinfo("Judul", "Pesan")` untuk info.
- `messagebox.showwarning("Judul", "Pesan")` untuk peringatan.
- `messagebox.showerror("Judul", "Pesan")` untuk error.
- `messagebox.askyesno("Judul", "Pesan")` untuk konfirmasi (Yes/No).

## Contoh Program
Lihat kode pada file `09_messagebox_tkinter.py` berikut:

```python
import tkinter as tk
from tkinter import messagebox

def tampilkan_info():
    messagebox.showinfo("Info", "Ini adalah kotak pesan informasi.")

def tampilkan_konfirmasi():
    hasil = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin?")
    if hasil:
        label.config(text="Anda memilih Yes.")
    else:
        label.config(text="Anda memilih No.")

root = tk.Tk()
root.title("Contoh MessageBox Tkinter")

button1 = tk.Button(root, text="Tampilkan Info", command=tampilkan_info)
button1.pack(pady=5)

button2 = tk.Button(root, text="Tampilkan Konfirmasi", command=tampilkan_konfirmasi)
button2.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=5)

root.mainloop()
```

Program di atas akan menampilkan dua tombol untuk menampilkan kotak pesan info dan konfirmasi.
