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
    print()

    while True:

        while True:
            try:
                pertama = float(input("Masukkan angka pertama: "))
                kedua = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Masukkan angka yang valid.")
                continue
            break

        while True:
            try:
                pilihan = input("Anda ingin kalkulasi apa? (+, -, *, /): ")
                if pilihan in ("+","-","*","/"):
                    break
                print("Pilih salah satu komputasi yang tersedia.")
            except ValueError:
                print("Masukkan pilihan yang valid.")
                continue
        print()

        if pilihan == "+":
            hasil = kalkulat_tambah(pertama,kedua)
            print(f"Hasil dari {pertama} + {kedua} = {hasil:.2f}")
        elif pilihan == "-":
            hasil = kalkulat_kurang(pertama,kedua)
            print(f"Hasil dari {pertama} - {kedua} = {hasil:.2f}")
        elif pilihan == "*":
            hasil = kalkulat_kali(pertama,kedua)
            print(f"Hasil dari {pertama} * {kedua} = {hasil:.2f}")
        elif pilihan == "/":
            try:
                hasil = kalkulat_bagi(pertama,kedua)
            except ZeroDivisionError:
                print("Tidak bisa membagi dengan nol!")
            else:
                print(f"Hasil dari {pertama} / {kedua} = {hasil:.2f}")

        while True:
            answer = input("Ingin lanjut kalkulasi? (y/n): ")
            if answer in ("y", "n"):
                print()
                break
            print("Tolong masukkan 'y' untuk ya atau 'n' untuk tidak.")
        if answer == "n":
            print("Terima kasih telah menggunakan Kalkulat. Senang bisa membantu.")
            return

if __name__ == "__main__":
    main()
