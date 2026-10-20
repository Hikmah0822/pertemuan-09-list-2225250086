# Input: List data numerik
# Proses: Mendefinisikan fungsi untuk menghitung rata-rata dengan penanganan list kosong (edge case handling)
# Output: Menampilkan hasil rata-rata dengan format dua angka di belakang koma

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

nilai = [75, 80, 65, 90, 88]
print(f"Rata-rata = {rata_rata(nilai):.2f}")