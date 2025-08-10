import tkinter as tk

def tampilkan_pilihan():
    label.config(text=f"Pilihan: {var.get()}")

root = tk.Tk()
root.title("Contoh OptionMenu Tkinter")

var = tk.StringVar(value="Python")
menu = tk.OptionMenu(root, var, "Python", "Java", "C++")
menu.pack(pady=10)

button = tk.Button(root, text="Tampilkan Pilihan", command=tampilkan_pilihan)
button.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=5)

root.mainloop()
