# Kotak Dialog Buka File di Tkinter

## Penjelasan
Tkinter menyediakan modul `filedialog` untuk membuka kotak dialog file, sehingga pengguna dapat memilih file dari sistem mereka. Ini sangat berguna untuk aplikasi yang membutuhkan input file dari user.

### Cara Menggunakan filedialog
Import modul `filedialog` dari `tkinter`:

```python
from tkinter import filedialog
```

Gunakan fungsi `askopenfilename()` untuk membuka dialog pemilihan file:

```python
filename = filedialog.askopenfilename(title="Pilih file", filetypes=[("All Files", "*.*"), ("Teks", "*.txt")])
```

## Contoh Program
Lihat kode pada file `11_filedialog_tkinter.py` berikut:

```python
import tkinter as tk
from tkinter import filedialog

def buka_file():
    filename = filedialog.askopenfilename(title="Pilih file", filetypes=[("All Files", "*.*"), ("Teks", "*.txt")])
    if filename:
        label.config(text=f"File dipilih: {filename}")
    else:
        label.config(text="Tidak ada file dipilih.")

root = tk.Tk()
root.title("Contoh File Dialog Tkinter")

button = tk.Button(root, text="Buka File", command=buka_file)
button.pack(pady=10)

label = tk.Label(root, text="Belum ada file dipilih.")
label.pack(pady=10)

root.mainloop()
```

Program di atas akan menampilkan tombol untuk membuka file dan menampilkan path file yang dipilih.
