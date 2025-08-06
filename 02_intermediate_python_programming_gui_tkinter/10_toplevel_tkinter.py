import tkinter as tk

def buka_jendela_baru():
    window = tk.Toplevel(root)
    window.title("Jendela Baru")
    label = tk.Label(window, text="Ini adalah jendela baru!")
    label.pack(padx=20, pady=20)

root = tk.Tk()
root.title("Contoh Jendela Baru Tkinter")

button = tk.Button(root, text="Buka Jendela Baru", command=buka_jendela_baru)
button.pack(pady=20)

root.mainloop()
