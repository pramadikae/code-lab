# Tombol Radio di Tkinter

## Penjelasan
Tombol radio (RadioButton) digunakan untuk memilih satu dari beberapa opsi. Jika satu tombol radio dipilih, yang lain akan otomatis tidak terpilih. Cocok untuk pilihan tunggal seperti jenis kelamin, status, dsb.

### Cara Membuat Tombol Radio
Gunakan `tk.Radiobutton()` dan variabel kontrol (`tk.IntVar()` atau `tk.StringVar()`) untuk mengelola nilai yang dipilih.

```python
var = tk.StringVar()
rb1 = tk.Radiobutton(root, text="Opsi 1", variable=var, value="1")
rb2 = tk.Radiobutton(root, text="Opsi 2", variable=var, value="2")
```

## Contoh Program
Lihat kode pada file `08_radiobutton_tkinter.py` berikut:

```python
import tkinter as tk

def tampilkan_pilihan():
    label_hasil.config(text=f"Pilihan: {var.get()}")

root = tk.Tk()
root.title("Contoh RadioButton Tkinter")

var = tk.StringVar(value="")

rb1 = tk.Radiobutton(root, text="Python", variable=var, value="Python")
rb1.pack(anchor=tk.W)
rb2 = tk.Radiobutton(root, text="Java", variable=var, value="Java")
rb2.pack(anchor=tk.W)
rb3 = tk.Radiobutton(root, text="C++", variable=var, value="C++")
rb3.pack(anchor=tk.W)

button = tk.Button(root, text="Tampilkan Pilihan", command=tampilkan_pilihan)
button.pack(pady=5)

label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=5)

root.mainloop()
```

Program di atas akan menampilkan tiga tombol radio dan menampilkan pilihan yang dipilih saat tombol ditekan.
