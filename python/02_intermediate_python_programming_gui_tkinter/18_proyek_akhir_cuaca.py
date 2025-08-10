# === 1. IMPORT LIBRARY ===
# Mengimpor library yang diperlukan
import tkinter as tk  # Untuk membuat antarmuka grafis (GUI)
from tkinter import messagebox, ttk  # messagebox untuk notifikasi, ttk untuk widget Treeview
import requests  # Untuk melakukan permintaan HTTP ke API cuaca
import sqlite3  # Untuk berinteraksi dengan database SQLite
from datetime import datetime  # Untuk mendapatkan waktu saat ini

# === 2. KONFIGURASI ===
# Variabel global untuk konfigurasi aplikasi
API_KEY = "YOUR_API_KEY"  # Ganti dengan API key Anda dari OpenWeatherMap
DB_NAME = "weather_history.db"  # Nama file database untuk menyimpan riwayat

# === 3. FUNGSI LOGIKA & DATABASE ===
# Kumpulan fungsi yang menangani logika aplikasi dan interaksi database

def get_weather(city):
    """Mengambil data cuaca dari OpenWeatherMap API berdasarkan nama kota."""
    # Periksa apakah API Key sudah diisi
    if not API_KEY or API_KEY == "YOUR_API_KEY":
        messagebox.showerror("Error", "API Key belum diatur. Silakan ganti 'YOUR_API_KEY' di dalam kode.")
        return None
    
    # URL endpoint API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=id"
    
    try:
        # Lakukan permintaan GET ke URL
        response = requests.get(url)
        response.raise_for_status()  # Jika status kode adalah error (4xx atau 5xx), akan memunculkan exception
        return response.json()  # Kembalikan data cuaca dalam format JSON
    # Tangani berbagai jenis error yang mungkin terjadi saat request
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", f"Kota '{city}' tidak ditemukan. Silakan coba lagi.")
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "Gagal terhubung ke server. Periksa koneksi internet Anda.")
    except requests.exceptions.Timeout:
        messagebox.showerror("Error", "Permintaan timeout. Server terlalu lama merespons.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat mengambil data: {e}")
    return None

def save_to_history(city, temperature, description):
    """Menyimpan riwayat pencarian cuaca ke dalam database SQLite."""
    conn = sqlite3.connect(DB_NAME)  # Buat koneksi ke database
    c = conn.cursor()  # Buat objek cursor untuk eksekusi perintah SQL
    # Perintah SQL untuk memasukkan data baru ke tabel 'history'
    c.execute("""
        INSERT INTO history (city, temperature, description, search_time)
        VALUES (?, ?, ?, ?)
    """, (city, temperature, description, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()  # Simpan perubahan ke database
    conn.close()  # Tutup koneksi

def setup_database():
    """Membuat tabel 'history' di database jika tabel tersebut belum ada."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Perintah SQL untuk membuat tabel jika belum ada (IF NOT EXISTS)
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL NOT NULL,
            description TEXT NOT NULL,
            search_time TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

# === 4. FUNGSI-FUNGSI UNTUK GUI ===
# Kumpulan fungsi yang dipanggil oleh widget di antarmuka

def search_weather():
    """Fungsi yang dipanggil saat tombol 'Cari' ditekan."""
    city = entry_city.get()  # Ambil teks dari kolom input kota
    if not city:
        messagebox.showwarning("Peringatan", "Nama kota tidak boleh kosong.")
        return  # Hentikan fungsi jika input kosong

    weather_data = get_weather(city)  # Panggil fungsi untuk mengambil data cuaca
    
    if weather_data:
        # Jika data berhasil didapat, ekstrak informasi yang relevan
        temp = weather_data['main']['temp']
        desc = weather_data['weather'][0]['description'].capitalize()
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        # Format string hasil untuk ditampilkan di label
        result_str = (
            f"Cuaca di {city.capitalize()}:\n"
            f"Suhu: {temp}°C\n"

            f"Deskripsi: {desc}\n"
            f"Kelembapan: {humidity}%\n"
            f"Kecepatan Angin: {wind_speed} m/s"
        )
        label_result.config(text=result_str)  # Update teks pada label hasil
        
        # Simpan hasil pencarian ke riwayat database
        save_to_history(city.capitalize(), temp, desc)
    else:
        # Jika data gagal didapat, tampilkan pesan error
        label_result.config(text="Gagal mengambil data cuaca.")

def show_history():
    """Menampilkan jendela baru (Toplevel) dengan riwayat pencarian dari database."""
    history_window = tk.Toplevel(root)  # Buat jendela baru di atas jendela utama
    history_window.title("Riwayat Pencarian")
    history_window.geometry("550x300")

    # Gunakan Treeview untuk menampilkan data dalam bentuk tabel
    tree = ttk.Treeview(history_window, columns=("Kota", "Suhu", "Deskripsi", "Waktu"), show="headings")
    tree.heading("Kota", text="Kota")
    tree.heading("Suhu", text="Suhu (°C)")
    tree.heading("Deskripsi", text="Deskripsi")
    tree.heading("Waktu", text="Waktu Pencarian")

    # Atur lebar kolom agar sesuai
    tree.column("Suhu", width=80, anchor="center")
    tree.column("Waktu", width=150)

    # Ambil semua data dari database
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT city, temperature, description, search_time FROM history ORDER BY search_time DESC")
    records = c.fetchall()  # Ambil semua baris hasil query
    conn.close()

    # Masukkan setiap baris data ke dalam Treeview
    for record in records:
        tree.insert("", "end", values=record)

    tree.pack(expand=True, fill="both")  # Tampilkan Treeview dan buat responsif

# === 5. SETUP GUI UTAMA ===
# Bagian ini membuat dan menata semua widget di jendela utama

root = tk.Tk()  # Buat instance jendela utama
root.title("Aplikasi Cuaca Sederhana")
root.geometry("400x300")

# Frame untuk input (mengelompokkan label, entry, dan tombol cari)
frame_input = tk.Frame(root, pady=10)
frame_input.pack()

label_city = tk.Label(frame_input, text="Masukkan Nama Kota:")
label_city.pack(side="left", padx=5)

entry_city = tk.Entry(frame_input, width=20)
entry_city.pack(side="left", padx=5)

button_search = tk.Button(frame_input, text="Cari", command=search_weather)
button_search.pack(side="left", padx=5)

# Frame untuk hasil (mengelompokkan label hasil)
frame_result = tk.Frame(root, pady=10)
frame_result.pack()

label_result = tk.Label(frame_result, text="Hasil akan ditampilkan di sini.", justify="left", font=("Helvetica", 12))
label_result.pack()

# Tombol untuk melihat riwayat
button_history = tk.Button(root, text="Lihat Riwayat", command=show_history)
button_history.pack(pady=20)

# === 6. INISIALISASI APLIKASI ===
# Blok utama yang akan dieksekusi saat script dijalankan

if __name__ == "__main__":
    setup_database()  # Pastikan tabel database sudah siap sebelum aplikasi berjalan
    root.mainloop()  # Jalankan event loop utama Tkinter untuk menampilkan GUI