# 🦟 Simulasi Penyebaran DBD (Demam Berdarah Dengue)
## Model SIR & Ross–Macdonald dengan Visualisasi Interaktif (Streamlit)

Proyek ini merupakan implementasi Tugas Akhir (TA-10) Mata Kuliah Pemrograman Model Numerik.  
Aplikasi mensimulasikan penyebaran penyakit DBD menggunakan dua model epidemiologi:

- **Model SIR (Susceptible–Infected–Recovered)**
- **Model Ross–Macdonald (Model Vektor untuk DBD)**

Aplikasi ini berbasis web menggunakan **Streamlit**, dengan tampilan modern **Glassmorphism UI**.

---

## 📌 Fitur Utama

### ✔ 1. Upload Dataset DBD (.csv)
- Sistem mendeteksi otomatis kolom tanggal & kasus.
- Mendukung dataset dengan format berbeda.

### ✔ 2. Simulasi Model Epidemiologi
- **SIR Model** (β, γ)
- **Ross–Macdonald Model** (a, b, c, μv)
- Fitting parameter otomatis dengan `curve_fit`
- Pemecahan ODE menggunakan `odeint`

### ✔ 3. Visualisasi Interaktif
- Grafik overlay:
  - Titik → Data asli
  - Garis → Model simulasi
- UI modern **Glassmorphism**
- Dashboard responsif Streamlit

### ✔ 4. Perhitungan Error (RMSE)
- Mengukur kecocokan model dengan data asli
- RMSE rendah → model baik

### ✔ 5. Prediksi 7 Hari ke Depan
- Menggunakan kondisi akhir model
- Plot prediksi  
- Tabel prediksi  
- Interpretasi otomatis

### ✔ 6. Interpretasi Parameter Otomatis
Contoh:
- β besar → penularan tinggi  
- γ → rata-rata durasi sakit (1/γ)  
- a, b, c → dinamika transmisi vektor  
- μv → umur nyamuk  

### ✔ 7. Analisis Tren dan Kesimpulan Otomatis

---

## 📂 Struktur Direktori

A10-Simulasi-DBD/
│── app.py # Aplikasi Streamlit (UI utama)
│── simulasidbd_core.py # Logika Model SIR & Ross-Macdonald
│── DATA DBD.csv # Dataset DBD
│── README.md # Dokumentasi (file ini)
│── requirements.txt # Instalasi library
│── Procfile # Deploy ke Heroku
│── render.yaml # Deploy ke Render
│── generate_report.py # (Opsional) Generator laporan otomatis

## 🔧 Instalasi & Menjalankan Program

### 1. Clone Repository
```bash
git clone https://github.com/username/TA10-Simulasi-DBD.git
cd TA10-Simulasi-DBD
### 2. Buat Virtual Environment
python -m venv venv
### 3. Aktivasi Environment
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
### 4. Install Dependencies
pip install -r requirements.txt
### 5. Jalankan Aplikasi Streamlit
streamlit run app.py

📊 Penjelasan Model
🔵 1. Model SIR
Persamaan:
dSdt=−βSI
dt
dS
=−βSI
dIdt=βSI−γI
dt
dI
=βSI−γI
dRdt=γI
dt
dR =γI
Parameter:
β (beta) = laju penularan
γ (gamma) = laju kesembuhan
Masa sakit = 1/γ

🟠 2. Model Ross–Macdonald
Digunakan untuk penyakit berbasis vektor (DBD).
Parameter:
a = frekuensi gigitan nyamuk
b = probabilitas manusia tertular
c = probabilitas nyamuk tertular
μv = laju kematian vektor
Persamaan mengikuti dinamika manusia (Sh, Ih, Rh) dan vektor (Sv, Iv).

📈 Visualisasi
Aplikasi menampilkan:
Data asli
Kurva SIR
Kurva Ross–Macdonald
Prediksi 7 hari
RMSE kedua model
Interpretasi otomatis tren & parameter
Tampilan menggunakan Glassmorphism agar modern dan estetis.

🔮 Prediksi 7 Hari Ke Depan
Aplikasi melakukan:
Mengambil titik akhir simulasi
Melakukan iterasi maju 7 hari
Menampilkan:
Kurva prediksi
Tabel prediksi
Kesimpulan tren naik/turun

📘 Interpretasi Model (Otomatis)
Program akan menjelaskan:
Arti parameter (β, γ, a, b, c, μv)
Tren data
Prediksi minggu depan
Hubungan model dengan realistis epidemiologi

📑 Catatan Dataset
Dataset harus memiliki:
Kolom tanggal
Kolom jumlah kasus
Jika kolom tidak bernama “Tanggal” atau “Kasus”, program akan mendeteksi otomatis.

🚀 Deployment
Deploy ke Heroku
web: streamlit run app.py
Deploy ke Render
Menggunakan file:
render.yaml

🤝 Kontribusi
Pull request dipersilakan — fitur tambahan seperti:
Model SEIR
Data cuaca
Prediksi jangka panjang
Heatmap parameter
sangat diterima.

📜 Lisensi
MIT License — bebas digunakan untuk edukasi & penelitian.

👤 Pembuat
Nama: Ardi Kamal Karima
NIM: 301230023
Mata Kuliah: Pemodelan Numerik
TA-10 – Simulasi DBD

⭐ Terima Kasih!
Silakan gunakan aplikasi ini untuk pembelajaran epidemiologi dan pemodelan matematika.
