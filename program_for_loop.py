# Membuat Program menggunakan For-loop, list dan Range

banyak = int(input("Berapa banyak data? "))

nama = []
umur = []

for i in range(0, banyak):
    print(f"Data ke {i+1}")
    input_nama = input("Nama : ")
    input_umur = int(input("Umur : "))

    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]

    print(f"{data_nama} Berumur {data_umur} Tahun")