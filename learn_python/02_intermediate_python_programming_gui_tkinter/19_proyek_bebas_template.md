# Proyek Bebas Tkinter

## Penjelasan
Pada bagian ini, Anda diberi kebebasan untuk membuat aplikasi GUI sederhana menggunakan Tkinter sesuai kreativitas Anda. Proyek bebas ini dapat berupa:
- Kalkulator sederhana
- To-Do List
- Aplikasi Catatan
- Stopwatch
- Game sederhana (Tebak Angka, Tic-Tac-Toe, dll)

### Langkah-langkah Umum
1. Tentukan ide aplikasi.
2. Rancang tampilan GUI (widget apa saja yang dibutuhkan).
3. Implementasikan logika program.
4. Tambahkan fitur tambahan sesuai kebutuhan.

## Contoh Template Proyek Bebas
Lihat kode pada file `19_proyek_bebas_template.py` berikut:

```python
import tkinter as tk

root = tk.Tk()
root.title("Proyek Bebas Tkinter")

# Tambahkan widget dan logika aplikasi Anda di sini
label = tk.Label(root, text="Selamat datang di Proyek Bebas!")
label.pack(pady=20)

# Contoh tombol
button = tk.Button(root, text="Klik Saya", command=lambda: label.config(text="Tombol diklik!"))
button.pack(pady=10)

root.mainloop()
```

Silakan kembangkan template di atas menjadi aplikasi sesuai ide Anda!
