pada soal pertama 

Untuk menambahkan fitur menampilkan nama mahasiswa dengan nilai akhir tertinggi, saya menambahkan dua variabel yaitu `nama_tertinggi` dan `nilai_tertinggi` pada fungsi `main()`.

Saya juga menambahkan kondisi perbandingan menggunakan `if` untuk membandingkan nilai akhir setiap mahasiswa. Apabila nilai mahasiswa lebih besar dari nilai tertinggi sebelumnya, program akan memperbarui nilai tertinggi beserta nama mahasiswanya.

Selanjutnya, fungsi `ringkasan()` diubah dengan menambahkan parameter nama dan nilai tertinggi agar dapat menampilkan informasi tersebut.

Fungsi `nilai_akhir()`, `nilai_huruf()`, `apakah_lulus()`, dan `proses_mahasiswa()` tidak perlu diubah karena tugas masing-masing sudah berjalan sesuai fungsinya.

Dengan pengelompokan tersebut, program menjadi lebih terstruktur, mudah dipahami, dan mudah dikembangkan apabila jumlah mahasiswa bertambah.



dan pada soal ke dua:
jika toko mengubah kebijakan pengiriman dari jarak sebelumnya 20 km menjadi 15 km 
biaya tambahan sebelumnya 5.000 sekarang menjadi 7.000

jadi kita harus mengubah bagian kode yang mengatur biaya jarak 

KODE SEBELUM PERUBAHAN 
def biaya_jarak(jarak):
    if jarak >= 20:
        return 5000
    return 0

KODE SESUDAH PERUBAHAN 
def biaya_jarak(jarak):
    if jarak >= 15:
        return 7000
    return 0