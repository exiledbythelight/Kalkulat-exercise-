def kalkulat_tambah(pertama,kedua): # Fungsi penambahan
    tambah = pertama + kedua # Rumus melakukan penambahan
    return tambah # Mengembalikan nilai hasil penambahan

def kalkulat_kurang(pertama,kedua): # Fungsi pengurangan
    kurang = pertama - kedua # Rumus melakukan pengurangan
    return kurang # Mengembalikan nilai hasil pengurangan

def kalkulat_kali(pertama,kedua): # Fungsi pengalian
    kali = pertama * kedua # Rumus melakukan pengalian
    return kali # Mengembalikan nilai hasil pengalian

def kalkulat_bagi(pertama,kedua): # Fungsi pembagian
    bagi = pertama / kedua # Rumus melakukan pembagian
    return bagi # Mengembalikan nilai hasil pembagian

def main(): # Fungsi utama
    print("Selamat datang di Kalkulat!") # Pesan pembuka
    print() # Beri jarak

    while True: # Loop utama

        while True: # Loop pertama
            try: # Mencoba meminta input dari user
                pertama = int(input("Masukkan angka pertama: ")) # Meminta input user untuk nilai pertama
                kedua = int(input("Masukkan angka kedua: ")) # Meminta input user untuk nilai kedua
            except ValueError: # Jika input bukan angka
                print("Masukkan angka yang valid.") # Tampilkan pesan error
                continue # Mengulangi input dan kembali ke loop pertama
            break # Keluar dari loop jika input valid

        while True: # Loop kedua
            try: # Mencoba meminta input dari user
                pilihan = input("Anda ingin kalkulasi apa? (+, -, *, /): ") # Meminta input user untuk jenis kalkulasi
                if pilihan in ("+","-","*","/"): # Jika user memilih salah satu jenis kalkulasi
                    break # Keluar dari loop jika input valid
                print("Pilih salah satu komputasi yang tersedia.") # Tampilkan pesan error
            except ValueError: # Jika mendeteksi ValueError
                print("Masukkan pilihan yang valid.") # Tampilkan pesan error
                continue # Mengulangi input dan kembali ke loop kedua
        print() # Beri jarak

        if pilihan == "+": # Jika user memilih "+"
            hasil = kalkulat_tambah(pertama,kedua) # Jalankan fungsi penambahan
            print(f"Hasil dari {pertama} + {kedua} = {hasil}") # Tampilkan hasil
        elif pilihan == "-": # Jika user memilih "-"
            hasil = kalkulat_kurang(pertama,kedua) # Jalankan fungsi pengurangan
            print(f"Hasil dari {pertama} - {kedua} = {hasil}") # Tampilkan hasil
        elif pilihan == "*": # Jika user memilih "*"
            hasil = kalkulat_kali(pertama,kedua) # Jalankan fungsi pengalian
            print(f"Hasil dari {pertama} * {kedua} = {hasil}") # Tampilkan hasil
        elif pilihan == "/": # Jika user memilih "/"
            try: # Mencoba meminta input dari user
                hasil = kalkulat_bagi(pertama,kedua) # Jalankan fungsi pembagian
            except ZeroDivisionError: # Mendeteksi masalah jika ada nilai nol
                print("Tidak bisa membagi dengan nol!") # Tampilkan pesan error
            else: # Jika tidak ada masalah
                print(f"Hasil dari {pertama} / {kedua} = {hasil}") # Tampilkan hasil

        while True: # Loop ketiga
            answer = input("Ingin lanjut kalkulasi? (y/n): ") # Menawarkan user untuk kalkulasi lagi
            if answer in ("y", "n"): # Jika mendeteksi input "y" dan "n"
                print() # Beri jarak
                break # Keluar dari loop jika input valid
            print("Tolong masukkan 'y' untuk ya atau 'n' untuk tidak.") # Tanpilkan pesan error jika input tidak valid
        if answer == "n": # Jika user input "n"
            print("Terima kasih telah menggunakan Kalkulat. Senang bisa membantu.") # Pesan penutup
            return # Keluar dari program

if __name__ == "__main__": # Jika file dijalankan langsung
    main() # Panggil fungsi utama
