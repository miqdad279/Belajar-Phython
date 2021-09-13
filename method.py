# Belajar Membuat Method / Function
# => tempat kita menyimpan kode blok
#   dimana, kode blok ini akan dieksekusi ketika kita memanggilnya

# Belum menggunakan method
nama = []

nama.append("Atikah")
print("============")
for data in nama:
    print(data)

nama.append("Amel")
print("============")
for data in nama:
    print(data)

nama.append("Farah")
print("============")
for data in nama:
    print(data)

# Menggunakan method

nama = []

def print_nama():
    print("============")
    for data in nama:
        print(data)

nama.append("Atikah")
print_nama()

nama.append("Amel")
print_nama()

nama.append("Farah")
print_nama()
