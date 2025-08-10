# Membuat Jendela Baru di Tkinter

## Penjelasan
Selain jendela utama, Anda dapat membuat jendela baru (window) di Tkinter menggunakan `tk.Toplevel()`. Jendela baru ini bisa digunakan untuk dialog, pengaturan, atau tampilan tambahan.

### Cara Membuat Jendela Baru
Gunakan `tk.Toplevel()` untuk membuat window baru:

```python
def buka_jendela_baru():
    window = tk.Toplevel(root)
    window.title("Jendela Baru")
    label = tk.Label(window, text="Ini adalah jendela baru!")
    label.pack(padx=20, pady=20)
```

## Contoh Program
Lihat kode pada file `10_toplevel_tkinter.py` berikut:

```python
import tkinter as tk

def buka_jendela_baru():
    window = tk.Toplevel(root)
    window.title("Jendela Baru")
    label = tk.Label(window, text="Ini adalah jendela baru!")
    label.pack(padx=20, pady=20)

root = tk.Tk()
root.title("Contoh Jendela Baru Tkinter")

button = tk.Button(root, text="Buka Jendela Baru", command=buka_jendela_baru)
button.pack(pady=20)

root.mainloop()
```

Program di atas akan menampilkan tombol yang jika diklik akan membuka jendela baru.
