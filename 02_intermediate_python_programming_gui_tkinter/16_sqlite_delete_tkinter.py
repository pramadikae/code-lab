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
