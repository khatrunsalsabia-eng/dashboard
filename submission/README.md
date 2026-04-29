# 📊 Proyek Analisis Data E-Commerce

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk melakukan analisis data pada dataset E-Commerce guna memahami pola penjualan, performa kategori produk, serta tren pembelian pelanggan. Hasil analisis ini diharapkan dapat memberikan insight yang dapat digunakan untuk pengambilan keputusan bisnis.

---

## 🎯 Pertanyaan Bisnis
1. Kategori produk apa yang memiliki kontribusi penjualan (revenue) tertinggi dan terendah?
2. Bagaimana tren penjualan bulanan selama periode dataset?

---

## 🛠️ Tahapan Analisis Data
### 1. Data Wrangling
* Menggabungkan beberapa dataset (orders, order_items, products)
* Mengidentifikasi permasalahan data:
  * Missing values
  * Data duplikat
* Membersihkan data:
  * Menghapus missing values
  * Menghapus duplikasi
  * Mengubah format tanggal

### 2. Exploratory Data Analysis (EDA)
* Analisis penjualan berdasarkan kategori produk
* Analisis tren penjualan berdasarkan waktu (bulanan)

### 3. Data Visualization
* Bar chart: Top kategori produk berdasarkan revenue
* Line chart: Tren penjualan bulanan

### 4. Conclusion & Recommendation
* Mengidentifikasi kategori dengan performa terbaik
* Menentukan periode penjualan tertinggi
* Memberikan rekomendasi strategi bisnis berbasis data

---

## 📁 Struktur Direktori
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── orders_dataset.csv
│   ├── order_items_dataset.csv
│   └── products_dataset.csv
├── notebook.ipynb
├── README.md
└── requirements.txt

Tentu, ini adalah isi lengkap untuk file `README.md` dalam format kode agar Anda bisa langsung menyalinnya (*copy-paste*) ke dalam editor teks Anda:

```markdown
# 📊 Proyek Analisis Data E-Commerce

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk melakukan analisis data pada dataset E-Commerce guna memahami pola penjualan, performa kategori produk, serta tren pembelian pelanggan. Hasil analisis ini diharapkan dapat memberikan insight yang dapat digunakan untuk pengambilan keputusan bisnis.

---

##  Pertanyaan Bisnis
1. Kategori produk apa yang memiliki kontribusi penjualan (revenue) tertinggi dan terendah?
2. Bagaimana tren penjualan bulanan selama periode dataset?

---

##  Tahapan Analisis Data
### 1. Data Wrangling
* Menggabungkan beberapa dataset (orders, order_items, products)
* Mengidentifikasi permasalahan data:
  * Missing values
  * Data duplikat
* Membersihkan data:
  * Menghapus missing values
  * Menghapus duplikasi
  * Mengubah format tanggal

### 2. Exploratory Data Analysis (EDA)
* Analisis penjualan berdasarkan kategori produk
* Analisis tren penjualan berdasarkan waktu (bulanan)

### 3. Data Visualization
* Bar chart: Top kategori produk berdasarkan revenue
* Line chart: Tren penjualan bulanan

### 4. Conclusion & Recommendation
* Mengidentifikasi kategori dengan performa terbaik
* Menentukan periode penjualan tertinggi
* Memberikan rekomendasi strategi bisnis berbasis data

---

## 📁 Struktur Direktori
```
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── orders_dataset.csv
│   ├── order_items_dataset.csv
│   └── products_dataset.csv
├── notebook.ipynb
├── README.md
└── requirements.txt
```

---

## ▶️ Cara Menjalankan Notebook
1. Buka file `notebook.ipynb` menggunakan:
   * Google Colab atau
   * Jupyter Notebook
2. Jalankan semua cell secara berurutan

---

## ▶️ Cara Menjalankan Dashboard

### 1. Persiapan Environment (Local)
Sangat disarankan untuk menggunakan *virtual environment* guna menghindari konflik versi antar library.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalasi Library
Pastikan Anda sudah berada di dalam virtual environment, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Dashboard Streamlit
```bash
streamlit run dashboard/dashboard.py
```

---

## 📦 Dependencies
* pandas
* numpy
* matplotlib
* seaborn
* streamlit

---

## 📊 Insight Utama
* Kategori produk tertentu mendominasi penjualan.
* Terdapat pola tren penjualan yang fluktuatif setiap bulan.
* Periode tertentu menunjukkan peningkatan signifikan dalam revenue.

---

## 💡 Rekomendasi
* Fokus pada pengembangan dan promosi kategori dengan revenue tinggi.
* Maksimalkan strategi pemasaran pada periode dengan tren penjualan tinggi.
* Evaluasi kategori dengan performa rendah untuk peningkatan atau penggantian strategi.

---

## ✨ Penutup
Proyek ini menunjukkan bagaimana data dapat digunakan untuk menghasilkan insight yang mendukung pengambilan keputusan bisnis secara lebih efektif dan berbasis bukti.
```
