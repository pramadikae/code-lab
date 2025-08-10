# Menu Dropdown di Tkinter

## Penjelasan
Menu dropdown (OptionMenu) digunakan untuk memilih satu opsi dari beberapa pilihan yang tersedia. Cocok untuk input pilihan seperti jenis kelamin, negara, dsb.

### Cara Membuat Menu Dropdown
Gunakan `tk.OptionMenu()` dan variabel kontrol (`StringVar`) untuk mengetahui nilai yang dipilih.

```python
var = tk.StringVar(value="Pilih")
menu = tk.OptionMenu(root, var, "Opsi1", "Opsi2", "Opsi3")
menu.pack()
```

## Contoh Program
Lihat kode pada file `14_optionmenu_tkinter.py` berikut:

```python
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
```

Program di atas akan menampilkan menu dropdown dan menampilkan pilihan yang dipilih saat tombol ditekan.
