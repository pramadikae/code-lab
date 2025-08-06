
# Proyek Akhir: Aplikasi Cuaca dengan Tkinter dan SQLite

Proyek ini adalah aplikasi desktop sederhana untuk mengecek cuaca yang dibuat dengan Python menggunakan library `tkinter` untuk antarmuka grafis (GUI) dan `sqlite3` untuk manajemen database.

## Fitur

1.  **Pencarian Cuaca Real-time**: Memasukkan nama kota untuk mendapatkan data cuaca terkini.
2.  **Tampilan Informasi Lengkap**: Menampilkan suhu, deskripsi cuaca, kelembapan, dan kecepatan angin.
3.  **Riwayat Pencarian**: Setiap pencarian yang berhasil akan disimpan ke dalam database SQLite.
4.  **Jendela Riwayat**: Menampilkan seluruh riwayat pencarian dalam jendela terpisah yang mudah dibaca.
5.  **Penanganan Error**: Memberikan notifikasi jika kota tidak ditemukan atau terjadi masalah koneksi.

## Komponen yang Digunakan

-   **Tkinter**: Untuk membuat semua elemen GUI seperti jendela, label, entry (input teks), tombol, dan frame.
-   **Requests**: Library pihak ketiga untuk melakukan permintaan HTTP ke API cuaca.
-   **SQLite3**: Untuk membuat dan mengelola database lokal yang menyimpan riwayat pencarian.
-   **OpenWeatherMap API**: Sebagai sumber data cuaca.

## Cara Menjalankan Aplikasi

1.  **Pastikan Library Terinstall**:
    Anda mungkin perlu menginstall library `requests`. Buka terminal atau command prompt dan jalankan:
    ```bash
    pip install requests
    ```

2.  **Dapatkan API Key**:
    -   Buat akun gratis di [OpenWeatherMap](https://openweathermap.org/appid).
    -   Dapatkan API key Anda dari dashboard akun Anda.

3.  **Masukkan API Key ke Kode**:
    -   Buka file `weather_app.py`.
    -   Cari baris `API_KEY = "YOUR_API_KEY"`.
    -   Ganti `"YOUR_API_KEY"` dengan API key yang sudah Anda dapatkan.

4.  **Jalankan File Python**:
    Buka terminal atau command prompt, arahkan ke direktori tempat file ini disimpan, lalu jalankan perintah:
    ```bash
    python weather_app.py
    ```

5.  **Gunakan Aplikasi**:
    -   Masukkan nama kota di kolom yang tersedia dan klik "Cari".
    -   Klik tombol "Lihat Riwayat" untuk melihat pencarian sebelumnya.

## Struktur Kode

-   **Fungsi Logika**: Terdiri dari fungsi-fungsi untuk mengambil data dari API (`get_weather`), menyimpan data ke database (`save_to_history`), dan inisialisasi database (`setup_database`).
-   **Fungsi GUI**: Terdiri dari fungsi-fungsi yang berinteraksi langsung dengan antarmuka, seperti `search_weather` yang dipanggil oleh tombol dan `show_history` untuk menampilkan jendela baru.
-   **Setup GUI Utama**: Bagian kode yang mendefinisikan dan menata semua widget Tkinter di jendela utama.
-   **Inisialisasi**: Blok `if __name__ == "__main__":` yang memastikan database di-setup sebelum aplikasi berjalan.
