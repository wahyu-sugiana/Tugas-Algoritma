
bobot_tugas = 0.3
bobot_uts = 0.3
bobot_uas = 0.4




def nilai_akhir(tugas, uts, uas):
    return tugas * bobot_tugas + uts * bobot_uts + uas * bobot_uas

def nilai_huruf(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70 and nilai_akhir < 85:
        return "B"
    elif nilai_akhir >= 55 and nilai_akhir < 70:
        return "C"
    elif nilai_akhir >= 40 and nilai_akhir < 55:
        return "D"
    else:
        return "E"

def apakah_lulus(nilai_huruf):
    return nilai_huruf in ("A", "B", "C")

def proses_mahasiswa(nama, tugas, uts, uas):
    akhir = nilai_akhir(tugas, uts, uas)
    huruf = nilai_huruf(akhir)
    if apakah_lulus(huruf):
        keterangan = "lulus"
    else:
        keterangan = "tidak lulus"

    print(nama + " Nilainya = " + str(akhir) + " " + "Predikatnya = " + str(huruf) + " " +keterangan)
    return akhir

def ringkasan(total_nilai, jumlah_lulus, jumlah_mahasiswa):
    print("rata rata nilai mahasiswa adalah = " + str(total_nilai/jumlah_mahasiswa))
    print("jumlah yang lulus = " + str(jumlah_lulus))

def main():
    total_nilai = 0
    jumlah_lulus = 0


    akhir = proses_mahasiswa("Andi", 80, 70, 90)
    total_nilai += akhir
    if apakah_lulus(nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("bunga", 90, 85, 88)
    total_nilai += akhir
    if apakah_lulus(nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("citra", 60, 45, 50)
    total_nilai += akhir
    if apakah_lulus(nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("dimas", 75, 80, 65)
    total_nilai += akhir
    if apakah_lulus(nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("eka", 30, 40, 35)
    total_nilai += akhir
    if apakah_lulus(nilai_huruf(akhir)):
        jumlah_lulus += 1


    
    print(ringkasan(total_nilai, jumlah_lulus, 1))






    
if __name__ == "__main__":
    main()