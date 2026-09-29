#KAKAP
"""hari ini masak apa king?
hari ini akan belajar tentang list di python
biar apa? biar commit di github awokawoka
(masih ai assited, tapi gapapa, yang penting bisa commit di github)
"""
#membuat list intinya
buah = ['apel', 'jeruk', 'mangga', 'pisang']
print(len(buah))  

# 2.(Indexing & Slicing)
print(buah[0])    # apel (item pertama)
print(buah[-1])   # pisang (item terakhir)
print(buah[1:3])  # ['jeruk', 'mangga'] (slicing/potong)

# 3. Mengubah & Mengecek Item
buah[0] = 'alpukat'     # Ubah item pertama jadi alpukat
print('jeruk' in buah)  # True (apakah jeruk ada di dalam list?)

# 4. Menambah Item
buah.append('anggur')     # Tambah di akhir -> ['alpukat', 'jeruk', 'mangga', 'pisang', 'anggur']
buah.insert(1, 'melon')   # Sisip di indeks ke-1 -> ['alpukat', 'melon', 'jeruk', ...]

# 5. Menghapus Item
buah.remove('jeruk')    # Hapus berdasarkan nama item
del buah[0]             # Hapus berdasarkan nomor indeks
buah.pop()              # Hapus item paling akhir
# buah.clear()          # Mengosongkan seluruh list

# 6. Menggabungkan List
angka1 = [1, 2]
angka2 = [3, 4]
gabung = angka1 + angka2  # [1, 2, 3, 4]

# 7. Mengurutkan & Membalikkan List
buah = ['pisang', 'apel', 'mangga']
buah.sort()             # Urutkan A-Z -> ['apel', 'mangga', 'pisang']
print("sorted list:", buah)
buah.reverse()          # Balikkan urutan -> ['pisang', 'mangga', 'apel']

buah.reverse()          # Balikkan urutan -> ['apel', 'mangga', 'pisang']   
print("reversed list:", buah)