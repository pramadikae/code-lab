# Menggunakan Ikon, Gambar, dan Tombol Keluar di Tkinter

## Penjelasan
Tkinter memungkinkan Anda menambahkan ikon pada jendela, menampilkan gambar, dan membuat tombol keluar (exit) untuk menutup aplikasi.

### Menambahkan Ikon pada Jendela
Gunakan method `iconbitmap()` untuk menambahkan ikon (format .ico) pada window:

```python
root.iconbitmap('icon.ico')
```

### Menampilkan Gambar
Gunakan modul `PhotoImage` untuk menampilkan gambar (format .gif atau .png):

```python
img = tk.PhotoImage(file='gambar.png')
label = tk.Label(root, image=img)
label.pack()
```

### Membuat Tombol Keluar
Gunakan tombol dengan command `root.quit` untuk keluar dari aplikasi:

```python
button = tk.Button(root, text="Keluar", command=root.quit)
button.pack()
```

## Contoh Program
Lihat kode pada file `05_ikon_gambar_exit_tkinter.py` berikut:

```python
import tkinter as tk

root = tk.Tk()
root.title("Contoh Ikon, Gambar, dan Tombol Keluar")

# Menambahkan ikon (pastikan file icon.ico ada di folder yang sama)
# root.iconbitmap('icon.ico')

# Menampilkan gambar (pastikan file gambar.png ada di folder yang sama)
# img = tk.PhotoImage(file='gambar.png')
# label_img = tk.Label(root, image=img)
# label_img.pack(pady=10)

label = tk.Label(root, text="Klik tombol di bawah untuk keluar.")
label.pack(pady=10)

button = tk.Button(root, text="Keluar", command=root.quit)
button.pack(pady=10)

root.mainloop()
```

Program di atas akan menampilkan label dan tombol keluar. Anda bisa mengaktifkan kode ikon dan gambar jika file tersedia.
