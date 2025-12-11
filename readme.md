# 🛡️ CipherForge - Blowfish Ultimate

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.30%2B-FF4B4B)
![Cryptography](https://img.shields.io/badge/Algorithm-Blowfish%20CBC-green)

Aplikasi kriptografi modern berbasis **Python** dan **Streamlit** untuk mengenkripsi dan mendekripsi file menggunakan algoritma **Blowfish**. Aplikasi ini dirancang dengan antarmuka *Cyberpunk/Sci-Fi* dan dilengkapi fitur benchmarking mendalam untuk analisis performa.

---

## ✨ Fitur Utama

### 🔐 Kriptografi
* **Algoritma:** Blowfish (Symmetric Block Cipher).
* **Mode Operasi:** CBC (Cipher Block Chaining).
* **Keamanan:** Mendukung kunci (key) dinamis 4-56 bytes.

### 🚀 Batch Processing (Multi-File)
* Upload **banyak file sekaligus** (misal: Kecil, Sedang, Besar).
* Enkripsi/Dekripsi semua file dalam satu klik.
* Download hasil output secara terpisah untuk setiap file.

### 📊 Precision Benchmark & Analytics
* **Uji Stabilitas:** Menjalankan algoritma 10x (iterasi) per file secara otomatis.
* **Grafik Interaktif:** Visualisasi *Stability Monitor* menggunakan **Altair** untuk melihat fluktuasi waktu eksekusi.
* **Tabel Detail:** Menampilkan waktu eksekusi per iterasi (ms), rata-rata, dan ukuran file.
* **Export CSV:** Unduh data hasil pengujian ke format `.csv` untuk laporan tugas/analisis.

### 🎨 Modern UI/UX
* Tema **Deep Space / Sci-Fi** dengan gradien warna gelap.
* Komponen UI *Glassmorphism* (efek kaca transparan).
* Tipografi *Monospace* untuk data teknis agar presisi.

---

## 🛠️ Instalasi & Cara Menjalankan

### Prasyarat
Pastikan **Python 3.x** sudah terinstall di komputer Anda.

### 1. Clone atau Download Project
Simpan semua file project di dalam satu folder.

### 2. Buat Virtual Environment (Disarankan)
Buat virtual environment untuk mengisolasi dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Library
Buka terminal/CMD di folder project, lalu jalankan:

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
Ketik perintah berikut di terminal:

```bash
streamlit run app.py
```
Aplikasi akan otomatis terbuka di browser Anda (biasanya di http://localhost:8501).

## 📂 Struktur Project

```
Kriptografi/
├── .gitignore          # Untuk mengignore agar tidak ikut masuk ke repository
├── app.py              # Source code utama aplikasi (Streamlit)
├── requirements.txt    # Daftar library yang dibutuhkan
├── file/ 
    ├── data_besar.txt  # File .txt berukuran 5MB
    ├── data_sedang.txt # File .txt berukuran 1MB
    └──  data_kecil.txt # file .txt berukuran 1kb
└── README.md           # Dokumentasi project ini
```

## 🧪 Panduan Pengujian (Skenario Tugas)
Untuk mendapatkan data laporan yang valid, ikuti langkah berikut:

1. **Siapkan Data Dummy**: Buat 3 file .txt dengan ukuran berbeda:
   - `kecil.txt` (1 KB)
   - `sedang.txt` (1 MB)
   - `besar.txt` (5 MB)

2. **Upload File**: Buka aplikasi, lihat sidebar sebelah kiri, dan upload ketiga file tersebut sekaligus.

3. **Masukkan Kunci**: Ketik kunci rahasia (contoh: `kripto`).

4. **Masuk ke Tab "PRECISION BENCHMARK"**: Klik tombol "ENGAGE BENCHMARK PROTOCOL".

5. **Analisis & Laporan**:
   - Lihat grafik garis untuk stabilitas.
   - Lihat tabel data untuk angka presisi.
   - Klik "Export Data Matrix (CSV)" untuk menyalin data ke laporan tugas Anda.

## 📸 Preview Aplikasi


## 📝 Catatan Teknis

- **Padding**: Aplikasi menggunakan standar padding PKCS#7 agar data sesuai dengan blok size Blowfish (8 byte).
- **Initialization Vector (IV)**: IV dibuat secara acak setiap kali enkripsi dan disisipkan di 8 byte pertama ciphertext (Prepend IV).
a
