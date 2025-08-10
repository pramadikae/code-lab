# Memperbarui Catatan dengan SQLite di Tkinter

## Penjelasan
Selain menambah dan menghapus data, Anda juga dapat memperbarui (update) catatan di database SQLite melalui aplikasi Tkinter. Biasanya, data yang akan diubah dipilih dari daftar, lalu diedit melalui input.

### Cara Memperbarui Data
1. Tampilkan data dari database (misal, dalam Listbox).
2. Pilih data yang akan diubah.
3. Tampilkan data di Entry untuk diedit.
4. Simpan perubahan ke database dengan perintah SQL `UPDATE`.

## Contoh Program
Lihat kode pada file `17_sqlite_update_tkinter.py` berikut:

```python
import tkinter as tk
import sqlite3

conn = sqlite3.connect('data_mahasiswa.db')
cursor = conn.cursor()

def tampilkan_data():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, nama, nim FROM mahasiswa")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]} ({row[2]})")

def pilih_data(event):
    pilihan = listbox.curselection()
    if pilihan:
        data = listbox.get(pilihan[0])
        id_, sisa = data.split(' - ')
        nama, nim = sisa.rsplit(' (', 1)
        nim = nim.rstrip(')')
        entry_nama.delete(0, tk.END)
        entry_nama.insert(0, nama.strip())
        entry_nim.delete(0, tk.END)
        entry_nim.insert(0, nim.strip())
        label_status.config(text=f"Edit data ID: {id_}")
        entry_nama.id_terpilih = id_
    else:
        entry_nama.id_terpilih = None

def update_data():
    id_ = getattr(entry_nama, 'id_terpilih', None)
    if id_:
        nama = entry_nama.get()
        nim = entry_nim.get()
        cursor.execute("UPDATE mahasiswa SET nama=?, nim=? WHERE id=?", (nama, nim, id_))
        conn.commit()
        tampilkan_data()
        label_status.config(text="Data berhasil diperbarui!")
    else:
        label_status.config(text="Pilih data yang akan diubah.")

root = tk.Tk()
root.title("Update Data SQLite Tkinter")

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)
listbox.bind('<<ListboxSelect>>', pilih_data)

tampilkan_data()

label1 = tk.Label(root, text="Nama:")
label1.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label2 = tk.Label(root, text="NIM:")
label2.pack()
entry_nim = tk.Entry(root)
entry_nim.pack()

button = tk.Button(root, text="Update Data", command=update_data)
button.pack(pady=5)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)

root.mainloop()

conn.close()
```

Program di atas akan menampilkan data, memungkinkan memilih data, mengedit, dan memperbarui ke database.
