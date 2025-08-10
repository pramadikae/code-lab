import tkinter as tk

root = tk.Tk()
root.title("Contoh Status Bar Tkinter")
root.geometry("300x200")

label = tk.Label(root, text="Aplikasi dengan Status Bar")
label.pack(pady=20)

status = tk.Label(root, text="Siap", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
