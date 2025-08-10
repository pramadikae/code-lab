import tkinter as tk

def halo():
    label.config(text="Halo, kamu menekan tombol!")

root = tk.Tk()
root.title("Contoh Tombol Tkinter")

label = tk.Label(root, text="Belum ada aksi.")
label.pack(pady=10)

button = tk.Button(root, text="Klik Saya", command=halo)
button.pack(pady=10)

root.mainloop()
