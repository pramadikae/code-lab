# Menambahkan Status Bar di Tkinter

## Penjelasan
Status bar adalah area di bagian bawah jendela aplikasi yang biasanya digunakan untuk menampilkan informasi status atau pesan kepada pengguna. Di Tkinter, status bar dapat dibuat menggunakan widget `Label` dan ditempatkan di bagian bawah dengan `pack(side=tk.BOTTOM, fill=tk.X)`.

### Cara Membuat Status Bar
Gunakan widget `Label` dan atur posisinya di bawah:

```python
status = tk.Label(root, text="Siap", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)
```

- `bd=1` : ketebalan border.
- `relief=tk.SUNKEN` : tampilan cekung.
- `anchor=tk.W` : rata kiri.
- `fill=tk.X` : memenuhi lebar window.

## Contoh Program
Lihat kode pada file `06_statusbar_tkinter.py` berikut:

```python
import tkinter as tk

root = tk.Tk()
root.title("Contoh Status Bar Tkinter")
root.geometry("300x200")

label = tk.Label(root, text="Aplikasi dengan Status Bar")
label.pack(pady=20)

status = tk.Label(root, text="Siap", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
```

Program di atas akan menampilkan status bar di bagian bawah window.
