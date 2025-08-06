import tkinter as tk

root = tk.Tk()
root.title("Proyek Bebas Tkinter")

# Tambahkan widget dan logika aplikasi Anda di sini
label = tk.Label(root, text="Selamat datang di Proyek Bebas!")
label.pack(pady=20)

# Contoh tombol
button = tk.Button(root, text="Klik Saya", command=lambda: label.config(text="Tombol diklik!"))
button.pack(pady=10)

root.mainloop()
