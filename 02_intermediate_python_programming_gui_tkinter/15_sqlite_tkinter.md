# Menggunakan Database di Tkinter (SQLite)

## Penjelasan
Tkinter dapat diintegrasikan dengan database SQLite untuk menyimpan dan mengelola data secara lokal. Modul `sqlite3` sudah tersedia di Python dan mudah digunakan.

### Cara Menggunakan SQLite di Tkinter
1. Import modul `sqlite3`.
2. Buat koneksi ke database.
3. Buat tabel jika belum ada.
4. Tambahkan data dari input Tkinter ke database.

## Contoh Program
Lihat kode pada file `15_sqlite_tkinter.py` berikut:

```python
import tkinter as tk
import sqlite3

# Membuat/membuka database
conn = sqlite3.connect('data_mahasiswa.db')
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS mahasiswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    nim TEXT
)''')
conn.commit()

def simpan_data():
    nama = entry_nama.get()
    nim = entry_nim.get()
    cursor.execute("INSERT INTO mahasiswa (nama, nim) VALUES (?, ?)", (nama, nim))
    conn.commit()
    label_status.config(text="Data berhasil disimpan!")

root = tk.Tk()
root.title("Contoh SQLite Tkinter")

label1 = tk.Label(root, text="Nama:")
label1.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label2 = tk.Label(root, text="NIM:")
label2.pack()
entry_nim = tk.Entry(root)
entry_nim.pack()

button = tk.Button(root, text="Simpan", command=simpan_data)
button.pack(pady=5)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)

root.mainloop()

conn.close()
```

Program di atas akan menyimpan data nama dan NIM ke database SQLite lokal.
