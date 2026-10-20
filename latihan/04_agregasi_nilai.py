# Input: List nilai numerik
# Proses: Menghitung total, rata-rata, nilai minimum, dan maksimum menggunakan fungsi built-in Python (sum, min, max, len)
# Output: Menampilkan hasil perhitungan agregasi nilai

nilai = [75, 80, 65, 90, 88]
print(f"Total = {sum(nilai)}")
print(f"Rata-rata = {sum(nilai)/len(nilai):.2f}")
print(f"Minimum = {min(nilai)}")
print(f"Maksimum = {max(nilai)}")