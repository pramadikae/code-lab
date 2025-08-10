import tkinter as tk
from tkinter import messagebox

def tampilkan_info():
    messagebox.showinfo("Info", "Ini adalah kotak pesan informasi.")

def tampilkan_konfirmasi():
    hasil = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin?")
    if hasil:
        label.config(text="Anda memilih Yes.")
    else:
        label.config(text="Anda memilih No.")

root = tk.Tk()
root.title("Contoh MessageBox Tkinter")

button1 = tk.Button(root, text="Tampilkan Info", command=tampilkan_info)
button1.pack(pady=5)

button2 = tk.Button(root, text="Tampilkan Konfirmasi", command=tampilkan_konfirmasi)
button2.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=5)

root.mainloop()
