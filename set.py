# Belajar Set

# hanya bisa menambah dan menghapus data 
# tidak akan menerima data yang duplikat (bersifat unic)
# Tidak dapat mengubah data pada index tertentu

nama = {"Atikah", "Amel", "Farah"}

nama.add("Hasna")
nama.add("Putri")

for data in nama:
    print(data)

nama.remove("Putri")
print("=================")

for data in nama:
    print(data)