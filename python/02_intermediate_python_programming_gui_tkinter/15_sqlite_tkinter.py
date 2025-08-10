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
