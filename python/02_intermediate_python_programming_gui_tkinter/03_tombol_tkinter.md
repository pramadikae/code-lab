# Membuat Tombol di Tkinter

## Penjelasan
Tombol (Button) adalah salah satu widget dasar di Tkinter yang digunakan untuk menjalankan aksi tertentu saat diklik. Anda dapat menambahkan tombol ke aplikasi dan menentukan fungsi yang akan dijalankan ketika tombol ditekan.

### Cara Membuat Tombol
Gunakan `tk.Button()` untuk membuat tombol. Anda bisa menentukan teks pada tombol dan fungsi yang dijalankan dengan parameter `command`.

```python
button = tk.Button(root, text="Klik Saya", command=nama_fungsi)
```

## Contoh Program
Lihat kode pada file `03_tombol_tkinter.py` berikut:

```python
import tkinter as tk

def halo():
    label.config(text="Halo, kamu menekan tombol!")

root = tk.Tk()
root.title("Contoh Tombol Tkinter")

label = tk.Label(root, text="Belum ada aksi.")
label.pack(pady=10)

button = tk.Button(root, text="Klik Saya", command=halo)
button.pack(pady=10)

root.mainloop()
```

Program di atas akan menampilkan tombol. Ketika tombol diklik, label akan berubah menjadi "Halo, kamu menekan tombol!".
