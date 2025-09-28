#Nama : Farah Hikmatul Maula
#NIM : 2509116099
#Minpro 2

user = { "Admin" : {"password": "admin123", "role": "admin"},
        "2509116000" :{"password": "12345", "role": "mahasiswa"}
    }

data_kehadiran = {}

#Menu Login
def login():
    print("-"*20)
    print("Selamat Datang")
    print("-"*20)
    while True:
        try:
            Nim = input("NIM/Username: ")
            Password = input("Password: ")
            
            if user[Nim]["password"] == Password and user[Nim]["role"] == "admin":
                print("Login berhasil")
                menu_admin()
            elif user[Nim]["password"] == Password and user[Nim]["role"] == "mahasiswa":
                print("Login Berhasil")
                menu_mahasiswa()
            return
        except Exception:
            print("Login gagal silahkan coba lagi")

data_mahasiswa = {}

def tambah_data():
    nama = (input("Nama Mahasiswa: "))
    nim = (input("NIM Mahasiswa: "))
    tl = (input("Tanggal Lahir Mahasiswa: "))
    angkatan = (input("Tahun Angkatan: "))

    data_mahasiswa[nim] = {
            "Nama" : nama,
            "NIM" : nim,
            "Tanggal Lahir" : tl,
            "Angkatan" : angkatan  
        }
    print("Data Berhasil Di Tambahkan")

def lihat_data():
    if data_mahasiswa:
        print("\n=== Data Mahasiswa ===")
        for nim, info in data_mahasiswa.items():
            print("Nama :", info["Nama"])
            print("NIM  :", info["NIM"])
            print("Tanggal Lahir :", info["Tanggal Lahir"])
            print("Angkatan       :", info["Angkatan"])

def update_data():
    nim = input("Masukkan NIM mahasiswa yang akan dicek kehadirannya: ")
    jam = float(input("Masukkan jam kehadiran: "))
    status = input("Apakah hadir? (tidak): ")

    if status == "tidak" and jam > 9.00:
        print("ALPA")
    else:
        print("Mahasiswa tepat waktu mengisi kehadiran")

def hapus_data():
    print("\n=== Hapus Data Mahasiswa ===")
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus")
    else:
        print("NIM tidak ditemukan.")

#Menu Admin
def menu_admin():
    while True:
        print("\n======== Menu Utama ========")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Keluar")
        print("\n")
        menu = input("Pilih menu (1/2/3/4/5): ")
        if menu == "1":
            tambah_data()

        elif menu == "2":
            lihat_data()

        elif menu == "3":
            update_data()
        
        elif menu == "4":
            hapus_data()

        elif menu == "5":
            print("Keluar Sistem")
            break
        

#Menu Mahasiswa/User
def menu_mahasiswa():
    while True:
        print("\n======== Menu Utama Catatan Kehadiran Mahasiswa ========")
        print("1. Masukkan Data")
        print("2. Keluar")
        print("\n")
        menu = input("Pilih Menu (1/2): ")
        if menu == "1":
            tanggal = input("Tanggal Kehadiran (1-30): ")
            bulan = input("Bulan Kehadiran (1-12): ")
            tahun = input("Tahun: ")
            jam = float(input("Jam kehadiran (08.00-09.00): "))
            print ("\n")
            status = input("Apakah hadir? (ya/tidak): ")

            if status == "ya":
                print("Hadir")
            elif status == "tidak":
                alasan_tidak_hadir = ("Sakit", "Izin", "Tidak Valid")
                print("S/I")
                alasan = input("Pilih Alasan: ")
                if alasan == "S":
                    print(alasan_tidak_hadir[0])
                elif alasan == "I":
                    print(alasan_tidak_hadir[1])
                else:
                    print(alasan_tidak_hadir[2])

        elif menu == "2":
            print("Keluar Terima Kasih")
            break
        else:
            print("Menu Tidak Valid Silahkan Coba Lagi")

login ()