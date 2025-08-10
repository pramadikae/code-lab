# Menambahkan Frame ke Program Anda di Tkinter

## Penjelasan
Frame adalah wadah (container) di Tkinter yang digunakan untuk mengelompokkan widget. Dengan Frame, Anda dapat mengatur layout aplikasi menjadi lebih terstruktur dan rapi, misalnya membagi window menjadi beberapa bagian.

### Cara Membuat Frame
Gunakan `tk.Frame()` untuk membuat frame, lalu tempatkan widget di dalamnya:

```python
frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Ini di dalam frame")
label.pack()
```

Anda bisa membuat beberapa frame dalam satu window.

## Contoh Program
Lihat kode pada file `07_frame_tkinter.py` berikut:

```python
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
```

Program di atas akan menampilkan dua frame dengan warna berbeda di kiri dan kanan window.
