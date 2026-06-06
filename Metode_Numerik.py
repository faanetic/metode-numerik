import matplotlib.pyplot as plt
import numpy as np

def interpolasi_linier(x0, y0, x1, y1, x_cari):
    kemiringan = (y1 - y0) / (x1 - x0)
    return y0 + kemiringan * (x_cari - x0)

def interpolasi_kuadratik(x0, y0, x1, y1, x2, y2, x_cari):
    b0 = y0
    b1 = (y1 - y0) / (x1 - x0)
    pembagi_atas = (y2 - y1) / (x2 - x1)
    b2 = (pembagi_atas - b1) / (x2 - x0)
    
    y_hasil = b0 + b1 * (x_cari - x0) + b2 * (x_cari - x0) * (x_cari - x1)
    return y_hasil, b0, b1, b2

# --- DATA HISTORIS UMKM KERIPIK SINGKONG ---
x_data = np.array([10, 30, 50])
y_data = np.array([150000, 550000, 750000])

x0, y0 = x_data[0], y_data[0]
x1, y1 = x_data[1], y_data[1]
x2, y2 = x_data[2], y_data[2]

# Target Produksi yang dicari
x_target = 25

# --- PERHITUNGAN NUMERIK ---
hasil_linier = interpolasi_linier(x0, y0, x1, y1, x_target)
hasil_kuadratik, b0, b1, b2 = interpolasi_kuadratik(x0, y0, x1, y1, x2, y2, x_target)

# --- PEMBUATAN GRAFIK (MATPLOTLIB) ---
# Pembuatan rentang nilai x yang halus untuk kurva kuadratik
x_kurva = np.linspace(10, 50, 200)

# Menghitung nilai y untuk sepanjang kurva linier (antara titik 0 dan 1)
y_kurva_linier = y0 + ((y1 - y0) / (x1 - x0)) * (x_kurva - x0)

# Menghitung nilai y untuk sepanjang kurva kuadratik (polinomial derajat 2)
y_kurva_kuadratik = b0 + b1 * (x_kurva - x0) + b2 * (x_kurva - x0) * (x_kurva - x1)

# Pengaturan kanvas grafik
plt.figure(figsize=(10, 6))

# 1. Plot Titik Data Asli (Historis)
plt.scatter(x_data, y_data, color='red', s=100, zorder=5, label='Data Historis UMKM')

# 2. Plot Garis Interpolasi Linier
plt.plot(x_kurva, y_kurva_linier, '--', color='orange', label='Garis Interpolasi Linier')

# 3. Plot Kurva Interpolasi Kuadratik
plt.plot(x_kurva, y_kurva_kuadratik, '-', color='blue', label='Kurva Interpolasi Kuadratik')

# 4. Plot Titik Hasil Estimasi (Target x = 25)
plt.scatter([x_target], [hasil_linier], color='gold', marker='X', s=150, zorder=6, 
            label=f'Estimasi Linier (x=25): Rp {hasil_linier:,.0f}')
plt.scatter([x_target], [hasil_kuadratik], color='green', marker='^', s=150, zorder=6, 
            label=f'Estimasi Kuadratik (x=25): Rp {hasil_kuadratik:,.0f}')

# Label & Judul Grafik
plt.title('Perbandingan Estimasi Keuntungan UMKM\n(Interpolasi Linier vs Kuadratik)', fontsize=14, fontweight='bold')
plt.xlabel('Volume Produksi (kg)', fontsize=12)
plt.ylabel('Keuntungan Bersih (Rp)', fontsize=12)

# Mengatur format angka pada sumbu Y agar menggunakan pemisah ribuan
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels([f'Rp {x:,.0f}' for x in current_values])

# Tambahan estetika
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='lower right', fontsize=10)

# Tampilkan grafik ke layar
plt.tight_layout()
plt.show()