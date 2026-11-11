
def biaya_berat(berat):
        if berat <= 2:
            return 10000
        return 10000 + (berat - 2) * 4000


def biaya_jarak(jarak):
    if jarak >= 20:
        return 5000
    return 0

def diskon (subtotal, anggota):
    if anggota:
        return subtotal * 10 // 100
    return 0 

def struk(nama, berat, jarak, anggota):
    b = biaya_berat(berat)
    j = biaya_jarak(jarak)
    d = diskon(b + j, anggota)
    ongkir = b + j - d
    print("sturk")
    print("Pelanggan    :", nama)
    print("Biaya berat  :", b)
    print("Biaya jarak  :", j)
    if d > 0:
        print("Potongan     :", d)
    print("Ongkir akhir :", ongkir)
    return ongkir







def main():
    total = 0
    
    
    
    total += struk("Rina", 1, 10, False)
    total += struk("Sari", 5, 25, False)
    total += struk("tono", 5, 25, True )
    total += struk("umar", 2, 30, True )
    total += struk("vina", 8, 15, False)



if __name__ == "__main__":
    main()