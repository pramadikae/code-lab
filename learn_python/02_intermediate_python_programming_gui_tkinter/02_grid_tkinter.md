# Penempatan dengan Sistem Grid Tkinter

## Penjelasan
Tkinter menyediakan beberapa metode untuk menempatkan widget di dalam window, salah satunya adalah `grid()`. Dengan sistem grid, Anda dapat menempatkan widget berdasarkan baris (row) dan kolom (column), mirip seperti tabel.

### Keunggulan Grid
- Memudahkan penataan layout secara terstruktur.
- Cocok untuk form atau tampilan yang membutuhkan susunan baris dan kolom.

### Cara Menggunakan grid()
Setiap widget dapat ditempatkan dengan menentukan parameter `row` dan `column`:

```python
widget.grid(row=0, column=0)
```

Anda juga bisa mengatur `padx`, `pady`, `columnspan`, dan `rowspan` untuk mengatur jarak dan lebar kolom/baris.

## Contoh Program
Lihat kode pada file `02_grid_tkinter.py` berikut:

```python
import tkinter as tk

root = tk.Tk()
root.title("Contoh Grid Tkinter")

label1 = tk.Label(root, text="Nama:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Email:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(root, text="Kirim")
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
```

Program di atas akan menampilkan form sederhana dengan dua label, dua input, dan satu tombol yang tersusun rapi menggunakan grid.
