import tkinter as tk

root = tk.Tk()
root.title("Contoh Grid Tkinter")

label1 = tk.Label(root, text="Nama:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Email:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(root, text="Kirim")
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
