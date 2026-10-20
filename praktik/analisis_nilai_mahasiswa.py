def rata_rata(data):
    """Menghitung rata-rata dari list data nilai.

    Menangani list kosong secara aman agar tidak terjadi error (ZeroDivisionError).
    """
    if not data:
        return 0.0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    """Menyaring dan mengembalikan list nilai mahasiswa yang lulus

    berdasarkan batas kelulusan tertentu (default = 60).
    """
    return [nilai for nilai in data if nilai >= batas]


# 1. Siapkan list nilai (minimal 10 nilai)
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# 2. Hitung banyak data menggunakan len
banyak_data = len(nilai)

# 3. Hitung total, minimum, maksimum, dan rata-rata
total_nilai = sum(nilai)
rata_rata_nilai = rata_rata(nilai)
min_nilai = min(nilai) if nilai else 0
max_nilai = max(nilai) if nilai else 0

# 4-5. Telusuri dan buat list nilai yang lulus
list_lulus = nilai_lulus(nilai, batas=60)
jumlah_lulus = len(list_lulus)

# 6. Hitung jumlah belum lulus dari total data dikurangi jumlah lulus
jumlah_belum_lulus = banyak_data - jumlah_lulus

# 7. Tampilkan seluruh hasil dengan format yang mudah dibaca
print("==================================================")
print("           RINGKASAN ANALISIS NILAI               ")
print("==================================================")
print(f"Seluruh Data Nilai   : {nilai}")
print(f"Banyak Data          : {banyak_data}")
print(f"Total Nilai          : {total_nilai}")
print(f"Rata-rata            : {rata_rata_nilai:.2f}")
print(f"Nilai Minimum        : {min_nilai}")
print(f"Nilai Maksimum       : {max_nilai}")
print(f"Batas Kelulusan      : 60")
print(f"Jumlah Lulus         : {jumlah_lulus}")
print(f"Jumlah Belum Lulus   : {jumlah_belum_lulus}")
print(f"List Nilai Lulus     : {list_lulus}")
print("==================================================")


# ==================================================
# PENGUJIAN TEST CASE WAJIB
# ==================================================
print("\n=== VALIDASI TEST CASE WAJIB ===")
test_cases = [[60, 70, 80], [59, 60, 61], []]

for idx, tc in enumerate(test_cases, 1):
  print(f"\nTest Case {idx} - Data: {tc}")
  avg = rata_rata(tc)
  print(f"Rata-rata            : {avg:.2f}")
  if tc:
    print(f"Minimum / Maksimum   : {min(tc)} / {max(tc)}")
    lulus_tc = nilai_lulus(tc, batas=60)
    print(f"Jumlah Lulus         : {len(lulus_tc)}")
  else:
    print("Status               : List kosong ditangani dengan aman (tidak error).")