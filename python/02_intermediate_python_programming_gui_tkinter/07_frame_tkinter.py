import tkinter as tk

root = tk.Tk()
root.title("Contoh Frame Tkinter")
root.geometry("350x200")

frame1 = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame2 = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

label1 = tk.Label(frame1, text="Ini Frame Kiri")
label1.pack(pady=10)

label2 = tk.Label(frame2, text="Ini Frame Kanan")
label2.pack(pady=10)

root.mainloop()
