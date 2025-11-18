def kalkulat_tambah(pertama,kedua):
    tambah = pertama + kedua
    return tambah

def kalkulat_kurang(pertama,kedua):
    kurang = pertama - kedua
    return kurang

def kalkulat_kali(pertama,kedua):
    kali = pertama * kedua
    return kali

def kalkulat_bagi(pertama,kedua):
    bagi = pertama / kedua
    return bagi

def main():
    print("Selamat datang di Kalkulat!")

    try:
        pertama = int(input("Masukkan angka pertama: "))
        kedua = int(input("Masukkan angka kedua: "))
    except ValueError:
        print("Masukkan angka yang valid.")
        return
    
    pilihan = input("Anda ingin kalkulasi apa? (+, -, *, /): ")

    if pilihan == "+":
        hasil = kalkulat_tambah(pertama,kedua)
        print(f"Hasil dari {pertama} + {kedua} = {hasil}")
    elif pilihan == "-":
        hasil = kalkulat_kurang(pertama,kedua)
        print(f"Hasil dari {pertama} - {kedua} = {hasil}")
    elif pilihan == "*":
        hasil = kalkulat_kali(pertama,kedua)
        print(f"Hasil dari {pertama} * {kedua} = {hasil}")
    elif pilihan == "/":
        hasil = kalkulat_bagi(pertama,kedua)
        print(f"Hasil dari {pertama} / {kedua} = {hasil}")
    else:
        print("Pilih salah satu komputasi yang tersedia.")

if __name__ == "__main__":
    main()
