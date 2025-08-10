# Slider di Tkinter

## Penjelasan
Slider (Scale) adalah widget di Tkinter yang memungkinkan pengguna memilih nilai dari rentang tertentu dengan menggeser tuas. Cocok untuk input angka seperti volume, brightness, dsb.

### Cara Membuat Slider
Gunakan `tk.Scale()` untuk membuat slider. Anda bisa mengatur orientasi, rentang nilai, dan fungsi yang dijalankan saat nilai berubah.

```python
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
slider.pack()
```

Untuk mendapatkan nilai slider, gunakan method `.get()`.

## Contoh Program
Lihat kode pada file `12_slider_tkinter.py` berikut:

```python
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
```

Program di atas akan menampilkan slider horizontal dan label yang menampilkan nilai slider saat digeser.
