# Proyek Akhir: Aplikasi Cuaca Sederhana dengan Tkinter

## Penjelasan
Pada proyek akhir ini, Anda akan membuat aplikasi cuaca sederhana menggunakan Tkinter. Aplikasi akan mengambil data cuaca dari API (misal: OpenWeatherMap) berdasarkan nama kota yang dimasukkan pengguna, lalu menampilkan hasilnya di jendela GUI.

### Langkah-langkah
1. Buat form input untuk nama kota.
2. Ambil data cuaca dari API menggunakan modul `requests`.
3. Tampilkan hasil cuaca di label.

> **Catatan:** Anda perlu mendaftar dan mendapatkan API key dari https://openweathermap.org/api (bisa gunakan key demo untuk latihan).

## Contoh Program
Lihat kode pada file `18_proyek_akhir_cuaca.py` berikut:

```python
import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"  # Ganti dengan API key Anda
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = entry_city.get()
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "id"}
    try:
        response = requests.get(URL, params=params)
        data = response.json()
        if data.get("cod") == 200:
            cuaca = data["weather"][0]["description"]
            suhu = data["main"]["temp"]
            label_result.config(text=f"Cuaca: {cuaca}\nSuhu: {suhu}°C")
        else:
            label_result.config(text="Kota tidak ditemukan.")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Aplikasi Cuaca Sederhana")

label = tk.Label(root, text="Masukkan nama kota:")
label.pack(pady=5)

entry_city = tk.Entry(root)
entry_city.pack(pady=5)

button = tk.Button(root, text="Cek Cuaca", command=get_weather)
button.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
```

Program di atas akan menampilkan form input kota, tombol cek cuaca, dan hasil cuaca dari API.

> **Pastikan Anda sudah menginstall modul `requests` dengan perintah:**
> 
> ```bash
> pip install requests
> ```
