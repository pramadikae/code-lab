import tkinter as tk

root = tk.Tk()
root.title("Contoh Ikon, Gambar, dan Tombol Keluar")

# Menambahkan ikon (pastikan file icon.ico ada di folder yang sama)
# root.iconbitmap('icon.ico')

# Menampilkan gambar (pastikan file gambar.png ada di folder yang sama)
# img = tk.PhotoImage(file='gambar.png')
# label_img = tk.Label(root, image=img)
# label_img.pack(pady=10)

label = tk.Label(root, text="Klik tombol di bawah untuk keluar.")
label.pack(pady=10)

button = tk.Button(root, text="Keluar", command=root.quit)
button.pack(pady=10)

root.mainloop()
