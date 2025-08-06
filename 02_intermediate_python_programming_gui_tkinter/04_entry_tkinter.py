import tkinter as tk

def tampilkan_nama():
    nama = entry.get()
    label_hasil.config(text=f"Halo, {nama}!")

root = tk.Tk()
root.title("Contoh Entry Tkinter")

label = tk.Label(root, text="Masukkan nama Anda:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Tampilkan", command=tampilkan_nama)
button.pack(pady=5)

label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=5)

root.mainloop()
