import tkinter as tk

def tampilkan_nilai(val):
    label.config(text=f"Nilai slider: {slider.get()}")

root = tk.Tk()
root.title("Contoh Slider Tkinter")

slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=tampilkan_nilai)
slider.pack(pady=10)

label = tk.Label(root, text="Nilai slider: 0")
label.pack(pady=10)

root.mainloop()
