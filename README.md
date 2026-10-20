# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: ...
NIM: ...
Kelas: ...

## Tujuan
Mengolah kumpulan data numerik dengan list Python[cite: 1].

## Struktur Program
* `latihan/01_buat_list.py`: Membuat dan menampilkan list beserta jumlah elemennya[cite: 1].
* `latihan/02_indeks_slicing.py`: Mengakses elemen list menggunakan indeks dan slicing[cite: 1].
* `latihan/03_manipulasi_list.py`: Melakukan perubahan, penambahan, penyisipan, dan penghapusan elemen[cite: 1].
* `latihan/04_agregasi_nilai.py`: Menghitung total, rata-rata, minimum, dan maksimum[cite: 1].
* `latihan/05_filter_kelulusan.py`: Menyaring nilai berdasarkan batas kelulusan[cite: 1].
* `latihan/06_fungsi_statistik.py`: Membuat fungsi kustom untuk perhitungan rata-rata[cite: 1].
* `praktik/analisis_nilai_mahasiswa.py`: Program utama analisis data mahasiswa[cite: 1].

## Cara Menjalankan
```bash
python3 praktik/analisis_nilai_mahasiswa.py
```[cite: 1]

## Test Case
Catat data, hasil yang diharapkan, hasil aktual, dan status[cite: 1].

| Data Yang Diperiksa | Hasil Yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| `[60, 70, 80]` | Rata-rata 70.00 | Rata-rata 70.00 | Pass |
| `[60, 70, 80]` | Minimum / maksimum 60 / 80 | Minimum / maksimum 60 / 80 | Pass |
| `[60, 70, 80]` | Jumlah lulus 3 | Jumlah lulus 3 | Pass |
| `[59, 60, 61]` | Batas kelulusan 2 lulus | 2 lulus | Pass |
| `[]` | Penanganan list kosong pada fungsi rata-rata (Tidak error) | Tidak error (Mengembalikan 0.0) | Pass |

## Refleksi
Tuliskan satu hal yang Anda pahami tentang indeks/list dan satu kesalahan yang berhasil diperbaiki[cite: 1].

* **Hal yang dipahami tentang indeks/list:** Penggunaan indeks negatif (`-1`) sangat membantu dalam mengakses elemen terakhir dari list secara langsung, dan teknik slicing memudahkan pengambilan bagian data tertentu.
* **Kesalahan yang berhasil diperbaiki:** Berhasil mengatasi potensi error `ZeroDivisionError` saat fungsi `rata_rata` menerima input list kosong dengan menambahkan pengecekan kondisi `if not data:` di dalam fungsi.