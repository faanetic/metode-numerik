import matplotlib.pyplot as plt
import numpy as np
import time  # Ditambahkan untuk menghitung waktu eksekusi komputasi

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

# Target Produksi yang dicari (Sesuai draf poster: 25 kg dan 40 kg)
x_target1 = 25
x_target2 = 40

print("="*65)
print("   PROGRAM INTERPOLASI NUMERIK - ESTIMASI KEUNTUNGAN UMKM")
print("="*65)

# --- MEMULAI PENGUKURAN WAKTU KOMPUTASI ---
waktu_mulai = time.perf_counter()

# Perhitungan untuk Target 1 (25 kg)
hasil_linier_25 = interpolasi_linier(x0, y0, x1, y1, x_target1)
hasil_kuadratik_25, b0, b1, b2 = interpolasi_kuadratik(x0, y0, x1, y1, x2, y2, x_target1)

# Perhitungan untuk Target 2 (40 kg)
hasil_linier_40 = interpolasi_linier(x0, y0, x1, y1, x_target2)
hasil_kuadratik_40, _, _, _ = interpolasi_kuadratik(x0, y0, x1, y1, x2, y2, x_target2)

waktu_selesai = time.perf_counter()
# --- AKHIR PENGUKURAN WAKTU ---

durasi_eksekusi = (waktu_selesai - waktu_mulai) * 1000 # Mengubah ke milidetik

# --- OUTPUT TERMINAL UNTUK SCREENSHOT ---
print(f" Data Historis Acuan UMKM:")
print(f"   * P0 = ({x0} kg, Rp {y0:,})")
print(f"   * P1 = ({x1} kg, Rp {y1:,})")
print(f"   * P2 = ({x2} kg, Rp {y2:,})")
print("-"*65)

print(f" [HASIL ESTIMASI PRODUKSI 25 KG]")
print(f"   > Interpolasi Linier    : Rp {hasil_linier_25:,.2f}")
print(f"   > Interpolasi Kuadratik : Rp {hasil_kuadratik_25:,.2f}")
print(f"   > Selisih Error         : Rp {abs(hasil_kuadratik_25 - hasil_linier_25):,.2f}")
print(f"   > Galat Relatif         : {abs(hasil_kuadratik_25 - hasil_linier_25)/hasil_kuadratik_25*100:.2f}%")
print("-"*65)

print(f" [HASIL ESTIMASI PRODUKSI 40 KG]")
print(f"   > Interpolasi Linier    : Rp {hasil_linier_40:,.2f}")
print(f"   > Interpolasi Kuadratik : Rp {hasil_kuadratik_40:,.2f}")
print(f"   > Selisih Error         : Rp {abs(hasil_kuadratik_40 - hasil_linier_40):,.2f}")
print(f"   > Galat Relatif         : {abs(hasil_kuadratik_40 - hasil_linier_40)/hasil_kuadratik_40*100:.2f}%")
print("-"*65)

# Poin Krusial untuk Pembuktian ke Dosen:
print(f"   Waktu eksekusi algoritma : {durasi_eksekusi:.4f} milidetik")
print("="*65)
print("\n[INFO] Menampilkan grafik visualisasi Matplotlib... Tutup jendela grafik untuk keluar.")

# --- PEMBUATAN GRAFIK (MATPLOTLIB) ---
x_kurva = np.linspace(10, 50, 200)
y_kurva_linier = y0 + ((y1 - y0) / (x1 - x0)) * (x_kurva - x0)
y_kurva_kuadratik = b0 + b1 * (x_kurva - x0) + b2 * (x_kurva - x0) * (x_kurva - x1)

plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='red', s=100, zorder=5, label='Data Historis UMKM')
plt.plot(x_kurva, y_kurva_linier, '--', color='orange', label='Garis Interpolasi Linier')
plt.plot(x_kurva, y_kurva_kuadratik, '-', color='blue', label='Kurva Interpolasi Kuadratik')

# Plot hasil estimasi target utama (25 kg)
plt.scatter([x_target1], [hasil_linier_25], color='gold', marker='X', s=150, zorder=6, 
            label=f'Estimasi Linier (25 kg): Rp {hasil_linier_25:,.0f}')
plt.scatter([x_target1], [hasil_kuadratik_25], color='green', marker='^', s=150, zorder=6, 
            label=f'Estimasi Kuadratik (25 kg): Rp {hasil_kuadratik_25:,.0f}')

plt.title('Perbandingan Estimasi Keuntungan UMKM\n(Interpolasi Linier vs Kuadratik)', fontsize=14, fontweight='bold')
plt.xlabel('Volume Produksi (kg)', fontsize=12)
plt.ylabel('Keuntungan Bersih (Rp)', fontsize=12)

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels([f'Rp {x:,.0f}' for x in current_values])
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='lower right', fontsize=10)
plt.tight_layout()
plt.show()