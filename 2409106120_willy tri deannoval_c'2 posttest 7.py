users = {}
current_user = None
purchases = []

while True:
    print("=== Registrasi ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users:
        print("Username sudah terdaftar, silakan coba lagi.")
    else:
        role = "admin" if len(users) == 0 else "user"
        users[username] = {'password': password, 'role': role}
        print(f"Registrasi berhasil! Role Anda: {role}")
        break

while True:
    print("\n=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username]['password'] == password:
        current_user = users[username]
        print(f"Login berhasil! Selamat datang, {username} ({current_user['role']})")
        break
    else:
        print("Username atau password salah, silakan coba lagi.")

while True:
    print("\n=== Menu ===")
    print("1. Tambah Pembelian")
    print("2. Tampilkan Pembelian")
    print("3. Update Pembelian")
    print("4. Hapus Pembelian")
    print("5. Logout")

    choice = input("Pilih menu (1-5): ")
    
    if choice == '1':  
        if current_user['role'] == "admin":
            item = input("Masukkan nama bahan: ")
            quantity = input("Masukkan jumlah: ")
            price = input("Masukkan harga: ")
            purchases.append({'item': item, 'quantity': quantity, 'price': price})
            print("Pembelian berhasil ditambahkan.")
        else:
            print("Hanya admin yang dapat menambah pembelian.")

    elif choice == '2':  
        print("\n=== Daftar Pembelian ===")
        for idx, purchase in enumerate(purchases, start=1):
            print(f"{idx}. Item: {purchase['item']}, Jumlah: {purchase['quantity']}, Harga: {purchase['price']}")
        if not purchases:
            print("Tidak ada pembelian yang tercatat.")

    elif choice == '3':  
        if current_user['role'] == "admin":
            try:
                idx = int(input("Masukkan nomor pembelian yang ingin diupdate: ")) - 1
                if 0 <= idx < len(purchases):
                    item = input("Masukkan nama bahan baru: ")
                    quantity = input("Masukkan jumlah baru: ")
                    price = input("Masukkan harga baru: ")
                    purchases[idx] = {'item': item, 'quantity': quantity, 'price': price}
                    print("Pembelian berhasil diupdate.")
                else:
                    print("Nomor pembelian tidak valid.")
            except ValueError:
                print("Input tidak valid. Harap masukkan nomor yang benar.")
        else:
            print("Hanya admin yang dapat mengupdate pembelian.")

    elif choice == '4':  
        if current_user['role'] == "admin":
            try:
                idx = int(input("Masukkan nomor pembelian yang ingin dihapus: ")) - 1
                if 0 <= idx < len(purchases):
                    purchases.pop(idx)
                    print("Pembelian berhasil dihapus.")
                else:
                    print("Nomor pembelian tidak valid.")
            except ValueError:
                print("Input tidak valid. Harap masukkan nomor yang benar.")
        else:
            print("Hanya admin yang dapat menghapus pembelian.")

    elif choice == '5':  
        print(f"Anda telah logout, {current_user}.")
        current_user = None
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
