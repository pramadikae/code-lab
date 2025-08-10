import tkinter as tk  # Import modul tkinter untuk GUI
import sqlite3        # Import modul sqlite3 untuk database SQLite

conn = sqlite3.connect('data_mahasiswa.db')  # Membuka koneksi ke database SQLite
cursor = conn.cursor()                       # Membuat objek cursor untuk eksekusi query

def tampilkan_data():
    # Menghapus semua item di listbox
    listbox.delete(0, tk.END)
    # Mengambil data mahasiswa dari database
    cursor.execute("SELECT id, nama, nim FROM mahasiswa")
    for row in cursor.fetchall():
        # Menampilkan data ke listbox dengan format: id - nama (nim)
        listbox.insert(tk.END, f"{row[0]} - {row[1]} ({row[2]})")

def pilih_data(event):
    # Fungsi ini dipanggil saat user memilih data di listbox
    pilihan = listbox.curselection()
    if pilihan:
        # Mengambil data yang dipilih
        data = listbox.get(pilihan[0])
        # Memecah string untuk mendapatkan id, nama, dan nim
        id_, sisa = data.split(' - ')
        nama, nim = sisa.rsplit(' (', 1)
        nim = nim.rstrip(')')
        # Menampilkan data ke entry
        entry_nama.delete(0, tk.END)
        entry_nama.insert(0, nama.strip())
        entry_nim.delete(0, tk.END)
        entry_nim.insert(0, nim.strip())
        # Menampilkan status dan menyimpan id yang dipilih
        label_status.config(text=f"Edit data ID: {id_}")
        entry_nama.id_terpilih = id_
    else:
        # Jika tidak ada data yang dipilih
        entry_nama.id_terpilih = None


def update_data():
    # Fungsi untuk mengupdate data mahasiswa di database
    id_ = getattr(entry_nama, 'id_terpilih', None)
    if id_:
        # Mengambil data dari entry
        nama = entry_nama.get()
        nim = entry_nim.get()
        # Update data di database
        cursor.execute("UPDATE mahasiswa SET nama=?, nim=? WHERE id=?", (nama, nim, id_))
        conn.commit()
        # Refresh tampilan listbox
        tampilkan_data()
        # Tampilkan status berhasil
        label_status.config(text="Data berhasil diperbarui!")
    else:
        # Jika belum memilih data
        label_status.config(text="Pilih data yang akan diubah.")

root = tk.Tk()  # Membuat window utama aplikasi
root.title("Update Data SQLite Tkinter")  # Judul window

listbox = tk.Listbox(root, width=40)  # Listbox untuk menampilkan data mahasiswa
listbox.pack(pady=10)
listbox.bind('<<ListboxSelect>>', pilih_data)  # Event saat memilih data di listbox

tampilkan_data()  # Menampilkan data pertama kali saat aplikasi dibuka


# Label dan entry untuk input nama
label1 = tk.Label(root, text="Nama:")
label1.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()


# Label dan entry untuk input NIM
label2 = tk.Label(root, text="NIM:")
label2.pack()
entry_nim = tk.Entry(root)
entry_nim.pack()


# Tombol untuk update data
button = tk.Button(root, text="Update Data", command=update_data)
button.pack(pady=5)


# Label untuk menampilkan status proses
label_status = tk.Label(root, text="")
label_status.pack(pady=5)

root.mainloop()  # Menjalankan aplikasi Tkinter

conn.close()  # Menutup koneksi database setelah aplikasi ditutup
