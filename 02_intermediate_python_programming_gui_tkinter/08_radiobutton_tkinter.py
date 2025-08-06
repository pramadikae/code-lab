import tkinter as tk

def tampilkan_pilihan():
    label_hasil.config(text=f"Pilihan: {var.get()}")

root = tk.Tk()
root.title("Contoh RadioButton Tkinter")

var = tk.StringVar(value="")

rb1 = tk.Radiobutton(root, text="Python", variable=var, value="Python")
rb1.pack(anchor=tk.W)
rb2 = tk.Radiobutton(root, text="Java", variable=var, value="Java")
rb2.pack(anchor=tk.W)
rb3 = tk.Radiobutton(root, text="C++", variable=var, value="C++")
rb3.pack(anchor=tk.W)

button = tk.Button(root, text="Tampilkan Pilihan", command=tampilkan_pilihan)
button.pack(pady=5)

label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=5)

root.mainloop()
