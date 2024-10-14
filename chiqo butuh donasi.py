users = {}
from prettytable import PrettyTable

# Untuk menampilkan pretty table
tabel = PrettyTable()
tabel.field_names = ["Nomor", "Nama Campaign", "Target Uang", "Saat Ini"]

# Campaign list untuk menyimpan data campaign
campaign_list = [
    ["1", "Chiqo ingin kaya", "2000000000", "10000"],
    ["2", "Chiqo ingin nikah", "128000000", "100000"],
    ["3", "Chiqo ingin hp baru", "30000000", "1210000"],
    ["4", "Chiqo ingin pc baru", "39000000", "21000"],
    ["5", "Chiqo ingin ke Paris", "20000000", "120000"],
]

# Fungsi untuk menambahkan data ke tabel
def update_table():
    tabel.clear_rows()
    for campaign in campaign_list:
        tabel.add_row(campaign)

update_table()

# Untuk Admin menambahkan campaign baru
def tambah_campaign():
    nomor_campaign = input("Masukkan Nomor Campaign: ")
    nama_campaign = input("Masukkan Nama Campaign: ")
    target_campaign = input("Masukkan Target yang ingin dicapai: ")
    sekarang_campaign = input("Berapa total yang sudah dicapai saat ini: ")

    # Tambah campaign ke list
    campaign_list.append([nomor_campaign, nama_campaign, target_campaign, sekarang_campaign])
    update_table()
    print(f"Campaign [{nama_campaign}] berhasil ditambahkan dengan target [Rp.{target_campaign}]")

#  melihat campaign
def lihat_campaign():
    print(tabel)

#  memperbarui campaign
def update_campaign():
    lihat_campaign()
    nomor_campaign = input("Masukkan nomor campaign yang ingin diperbarui: ")
    for campaign in campaign_list:
        if campaign[0] == nomor_campaign:
            print("Data lama:", campaign)
            campaign[1] = input("Masukkan Nama Campaign baru: ")
            campaign[2] = input("Masukkan Target Uang baru: ")
            campaign[3] = input("Masukkan Total yang sudah dicapai saat ini baru: ")
            update_table()
            print("Campaign berhasil diperbarui!")
            return
    print("Campaign tidak tertera dalam tabel.")

#  menghapus campaign
def hapus_campaign():
    lihat_campaign()
    nomor_campaign = input("Masukkan nomor campaign yang ingin dihapus: ")
    for campaign in campaign_list:
        if campaign[0] == nomor_campaign:
            campaign_list.remove(campaign)
            update_table()  # Perbarui tabel setelah penghapusan
            print(f"Campaign dengan nomor [{nomor_campaign}] berhasil dihapus.")
            return
    print("Campaign tidak tertera dalam tabel.")

# Admin
def admin():
    username = "chiqoganteng"
    password = "chiqosayangpraktisi"

    input_username = input("Username: ")
    input_password = input("Password: ")

    if input_username == username and input_password == password:
        print("=" * 30)
        print("       Login berhasil.      ")
        print("Selamat Datang Admin Ganteng")
        print("=" * 30)
        while True:
            print("\n=== Menu Admin ===")
            print("1. Tambah Campaign")
            print("2. Lihat Campaign")
            print("3. Update Campaign")
            print("4. Hapus Campaign")
            print("5. Logout")

            pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

            if pilihan == "1":
                tambah_campaign()
            elif pilihan == "2":
                lihat_campaign()
            elif pilihan == "3":
                update_campaign()
            elif pilihan == "4":
                hapus_campaign()
            elif pilihan == "5":
                print("=" * 35)
                print("Sampai jumpa lagi Admin Ganteng.")
                print("=" * 35)
                break
            else:
                print("Pilihan tidak valid.")
    else:
        print("Username atau password salah.")

# untuk menampilkan campaign ke donatur
def donasi():
    while True:
        print("Apakah anda ingin berdonasi?")
        pilihan = input("Masukan pilihan iya/tidak: ")
        
        if pilihan == "iya":
            lihat_campaign()
            nomor_campaign = input("Masukkan nomor campaign yang ingin didonasikan: ")
            for campaign in campaign_list:
                if campaign[0] == nomor_campaign:
                    try:
                        jumlah_donasi = int(input("Masukkan jumlah donasi: "))
                        # Update total yang sudah dicapai
                        total_sekarang = int(campaign[3])
                        campaign[3] = str(total_sekarang + jumlah_donasi)
                        update_table() 
                        print(f"Donasi sebesar Rp.{jumlah_donasi} berhasil untuk campaign [{campaign[1]}].")
                        return
                    except:
                            print("Input tidak valid, harap masukkan angka untuk jumlah donasi.")
                            return
            print("Campaign tidak tertera dalam tabel.")
        elif pilihan == "tidak":
            lihat_campaign()
            break
        else:
            print("Mohon maaf anda tidak valid")

#  untuk registrasi user
def registrasi_user(username, password):
    if username in users:
        print("Username sudah terdaftar.")
    else:
        users[username] = password
        print("=" * 41)
        print("Selamat Anda Telah Berhasil Membuat Akun!")
        print("=" * 41)

#  untuk login user
def login_user(username, password):
    if username in users and users[username] == password:
        donatur_menu()
    else:
        print("=" * 52)
        print("Username atau password salah, silahkan login kembali")
        print("=" * 52)

# menu donatur
def donatur_menu():
    print("=" * 30)
    print("      Login berhasil.    ")
    print("Selamat Datang Orang Baik")
    print("=" * 30)
    while True:
        print("=== Menu Orang Baik ===")
        print("1. Lihat Campaign")
        print("2. Logout")
        pilihan = input("Masukan pilihan 1/2: ")
        if pilihan == "1":
            donasi()
        elif pilihan == "2":
            print("=" * 65)
            print("Terima kasih atas kunjungannya, Semoga dilancarkan rejekinya!!!.")
            print("=" * 65)
            break
        else:
            print("Pilihan tidak valid.")

#  untuk login utama Admin / Donatur
def login():
    while True:
        print("Selamat Datang di Donasi Online")
        print("1. Admin")
        print("2. Donatur")
        print("3. Keluar")
        pilihan = input("Silahkan untuk memilih login sebagai apa: ")
        if pilihan == "1":
            admin()
        elif pilihan == "2":
            donatur()
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

#  donatur registrasi/login
def donatur():
    while True:
        print("\n1. Registrasi\n2. Login\n3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            registrasi_user(username, password)

        elif pilihan == "2":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            login_user(username, password)

        elif pilihan == "3":
            login()
            break

        else:
            print("Pilihan tidak valid.")

# Memulai program
login()
