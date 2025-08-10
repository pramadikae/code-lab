# Menghapus Catatan dari Database di Tkinter (SQLite)

## Penjelasan
Selain menambah data, Anda juga dapat menghapus catatan dari database SQLite melalui aplikasi Tkinter. Biasanya, data yang akan dihapus dipilih berdasarkan ID atau kriteria tertentu.

### Cara Menghapus Data
1. Tampilkan data dari database (misal, dalam Listbox).
2. Pilih data yang akan dihapus.
3. Hapus data dari database menggunakan perintah SQL `DELETE`.

## Contoh Program
Lihat kode pada file `16_sqlite_delete_tkinter.py` berikut:

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

def hapus_data():
    pilihan = listbox.curselection()
    if pilihan:
        data = listbox.get(pilihan[0])
        id_ = data.split(' - ')[0]
        cursor.execute("DELETE FROM mahasiswa WHERE id=?", (id_,))
        conn.commit()
        tampilkan_data()
        label_status.config(text="Data berhasil dihapus!")
    else:
        label_status.config(text="Pilih data yang akan dihapus.")

root = tk.Tk()
root.title("Hapus Data SQLite Tkinter")

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

tampilkan_data()

button = tk.Button(root, text="Hapus Data", command=hapus_data)
button.pack(pady=5)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)

root.mainloop()

conn.close()
```

Program di atas akan menampilkan data dari database dan menghapus data yang dipilih pada Listbox.
