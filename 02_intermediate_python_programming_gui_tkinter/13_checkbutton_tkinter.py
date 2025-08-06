import tkinter as tk

def tampilkan_status():
    hasil = []
    if var1.get(): hasil.append("Python")
    if var2.get(): hasil.append("Java")
    if var3.get(): hasil.append("C++")
    label.config(text="Dipilih: "+", ".join(hasil) if hasil else "Tidak ada")

root = tk.Tk()
root.title("Contoh Checkbutton Tkinter")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

cb1 = tk.Checkbutton(root, text="Python", variable=var1)
cb1.pack(anchor=tk.W)
cb2 = tk.Checkbutton(root, text="Java", variable=var2)
cb2.pack(anchor=tk.W)
cb3 = tk.Checkbutton(root, text="C++", variable=var3)
cb3.pack(anchor=tk.W)

button = tk.Button(root, text="Tampilkan Status", command=tampilkan_status)
button.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=5)

root.mainloop()
