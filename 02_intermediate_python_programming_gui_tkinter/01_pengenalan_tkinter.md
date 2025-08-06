# Pengenalan Tkinter

## Apa itu Tkinter?
Tkinter adalah library standar Python untuk membuat aplikasi GUI (Graphical User Interface). Dengan Tkinter, Anda dapat membuat aplikasi desktop dengan tampilan grafis seperti tombol, label, input, dan lain-lain.

## Mengapa Menggunakan Tkinter?
- Mudah digunakan dan dipelajari.
- Sudah terintegrasi di Python (tidak perlu instalasi tambahan pada sebagian besar distribusi Python).
- Dokumentasi dan komunitas yang luas.

## Cara Instalasi dan Import Tkinter
Pada sebagian besar instalasi Python, Tkinter sudah tersedia. Untuk menggunakannya, cukup lakukan import:

```python
import tkinter as tk
```

Jika belum terinstal, Anda bisa menginstalnya (di Linux):
```bash
sudo apt-get install python3-tk
```

## Struktur Dasar Program Tkinter
1. Import modul Tkinter.
2. Membuat objek utama (root window).
3. Menjalankan event loop.

## Contoh Program Sederhana
Lihat kode pada file `01_pengenalan_tkinter.py` berikut:

```python
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("300x200")

root.mainloop()
```

Program di atas akan menampilkan jendela kosong berjudul "Hello Tkinter" dengan ukuran 300x200 piksel.
