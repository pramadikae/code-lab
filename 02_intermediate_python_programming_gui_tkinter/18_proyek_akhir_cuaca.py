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
