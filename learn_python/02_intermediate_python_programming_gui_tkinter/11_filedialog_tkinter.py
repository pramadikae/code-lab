import tkinter as tk
from tkinter import filedialog

def buka_file():
    filename = filedialog.askopenfilename(title="Pilih file", filetypes=[("All Files", "*.*"), ("Teks", "*.txt")])
    if filename:
        label.config(text=f"File dipilih: {filename}")
    else:
        label.config(text="Tidak ada file dipilih.")

root = tk.Tk()
root.title("Contoh File Dialog Tkinter")

button = tk.Button(root, text="Buka File", command=buka_file)
button.pack(pady=10)

label = tk.Label(root, text="Belum ada file dipilih.")
label.pack(pady=10)

root.mainloop()
