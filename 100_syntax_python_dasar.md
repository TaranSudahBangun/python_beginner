# 100 Syntax Python Paling Dasar dan Sederhana

Panduan kilat ini berisi 100 pola syntax Python paling dasar yang sangat cocok untuk pemula.

## I. Output dan Komentar
1. Mencetak teks ke layar:
```python
print("Halo Dunia")
```
2. Mencetak angka:
```python
print(123)
```
3. Mencetak hasil operasi matematika:
```python
print(5 + 5)
```
4. Mencetak beberapa nilai sekaligus:
```python
print("Nilai:", 90)
```
5. Menggunakan pemisah (separator) kustom:
```python
print("Python", "Sangat", "Mudah", sep="-")
```
6. Mengubah akhir cetakan (end):
```python
print("Halo", end=" ")
print("Dunia")
```
7. Komentar satu baris:
```python
# Ini adalah komentar
```
8. Komentar multi-baris (docstring):
```python
"""
Ini adalah komentar
lebih dari satu baris
"""
```
9. Mencetak string dengan tanda kutip tunggal:
```python
print('Belajar Python')
```
10. Menggabungkan string di dalam print:
```python
print("Hello " + "World")
```

## II. Variabel dan Tipe Data Dasar
11. Membuat variabel string:
```python
nama = "Budi"
```
12. Membuat variabel integer:
```python
umur = 20
```
13. Membuat variabel float:
```python
tinggi = 175.5
```
14. Membuat variabel boolean:
```python
aktif = True
```
15. Menampilkan nilai variabel:
```python
print(nama)
```
16. Mengecek tipe data dengan `type()`:
```python
print(type(umur))
```
17. Assignment ganda:
```python
x, y, z = 1, 2, 3
```
18. Assignment nilai yang sama ke banyak variabel:
```python
a = b = c = 10
```
19. Menghapus variabel dengan `del`:
```python
del x
```
20. Penamaan variabel dengan snake_case:
```python
nama_lengkap = "Ani"
```

## III. Operasi Aritmatika
21. Penjumlahan:
```python
hasil = 10 + 5
```
22. Pengurangan:
```python
hasil = 10 - 5
```
23. Perkalian:
```python
hasil = 10 * 5
```
24. Pembagian (float):
```python
hasil = 10 / 3
```
25. Pembagian bulat (floor division):
```python
hasil = 10 // 3
```
26. Modulus (sisa bagi):
```python
hasil = 10 % 3
```
27. Pangkat (eksponen):
```python
hasil = 2 ** 3
```
28. Prioritas operator (kurung):
```python
hasil = (2 + 3) * 4
```
29. Penambahan singkat:
```python
x = 5; x += 1
```
30. Pengurangan singkat:
```python
x = 5; x -= 1
```

## IV. Operasi String
31. Mengubah string menjadi huruf besar:
```python
teks = "halo".upper()
```
32. Mengubah string menjadi huruf kecil:
```python
teks = "HALO".lower()
```
33. Menghitung panjang string:
```python
panjang = len("Python")
```
34. Menggabungkan string (Concatenation):
```python
s = "A" + "B"
```
35. Mengulang string:
```python
s = "Ha" * 3
```
36. Mengakses karakter pertama string (Indexing):
```python
huruf = "Python"[0]
```
37. Mengambil sebagian string (Slicing):
```python
potong = "Python"[0:3]
```
38. Mengganti bagian string (Replace):
```python
baru = "Hello World".replace("World", "Python")
```
39. Memecah string menjadi list (Split):
```python
kata = "A,B,C".split(",")
```
40. Mengecek substring dengan `in`:
```python
ada = "Py" in "Python"
```

## V. Input Data dari Pengguna
41. Mengambil input teks dasar:
```python
nama = input("Masukkan nama: ")
```
42. Mengambil input dan langsung konversi ke integer:
```python
umur = int(input("Umur: "))
```
43. Mengambil input dan konversi ke float:
```python
berat = float(input("Berat: "))
```
44. Menampilkan f-string dengan input:
```python
print(f"Halo {nama}")
```
45. Menggunakan format string lama (`%`):
```python
print("Nama: %s" % nama)
```
46. Menggunakan metode `.format()`:
```python
print("Halo {}".format(nama))
```
47. Input string multi-baris (simulasi):
```python
teks = input("Ketik sesuatu: ")
```
48. Menampilkan input tanpa baris baru otomatis (di versi tertentu):
```python
print("Loading", end="...")
```
49. Membersihkan spasi pinggir input (`strip`):
```python
teks = input("Teks: ").strip()
```
50. Mengecek apakah input berupa angka (`isdigit`):
```python
cek = "123".isdigit()
```

## VI. Percabangan (If-Else)
51. If sederhana:
```python
if 5 > 2:
    print("Benar")
```
52. If-Else:
```python
if 2 > 5:
    print("Ya")
else:
    print("Tidak")
```
53. If-Elif-Else:
```python
nilai = 75
if nilai > 80:
    print("A")
elif nilai > 70:
    print("B")
else:
    print("C")
```
54. If bersarang (Nested If):
```python
if x > 0:
    if x % 2 == 0:
        print("Positif Genap")
```
55. Operator perbandingan sama dengan (`==`):
```python
hasil = (5 == 5)
```
56. Operator tidak sama dengan (`!=`):
```python
hasil = (5 != 3)
```
57. Operator lebih besar dari (`>`):
```python
hasil = (10 > 5)
```
58. Operator logika `and`:
```python
hasil = (True and False)
```
59. Operator logika `or`:
```python
hasil = (True or False)
```
60. Operator logika `not`:
```python
hasil = not(True)
```

## VII. Perulangan (Loops)
61. For loop dasar dengan range:
```python
for i in range(5):
    print(i)
```
62. For loop dengan batas awal dan akhir:
```python
for i in range(1, 6):
    print(i)
```
63. For loop dengan step:
```python
for i in range(0, 10, 2):
    print(i)
```
64. For loop iterasi string:
```python
for h in "Py":
    print(h)
```
65. While loop dasar:
```python
i = 1
while i <= 3:
    print(i)
    i += 1
```
66. Menggunakan perintah `break`:
```python
for i in range(5):
    if i == 3:
        break
```
67. Menggunakan perintah `continue`:
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
68. For loop dengan `else`:
```python
for i in range(3):
    print(i)
else:
    print("Selesai")
```
69. While loop dengan `else`:
```python
x = 0
while x < 2:
    x += 1
else:
    print("Loop habis")
```
70. Perulangan bersarang (Nested loop):
```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

## VIII. Struktur Data: List
71. Membuat list kosong:
```python
data = []
```
72. Membuat list berisi data:
```python
buah = ["apel", "jeruk", "mangga"]
```
73. Mengakses elemen list:
```python
item = buah[0]
```
74. Mengubah elemen list:
```python
buah[1] = "duku"
```
75. Menambah elemen di akhir (`append`):
```python
buah.append("pisang")
```
76. Menambah elemen di posisi tertentu (`insert`):
```python
buah.insert(0, "semangka")
```
77. Menghapus elemen berdasarkan nilai (`remove`):
```python
buah.remove("apel")
```
78. Menghapus elemen berdasarkan indeks (`pop`):
```python
buah.pop(0)
```
79. Menghitung jumlah elemen list (`len`):
```python
jumlah = len(buah)
```
80. Mengurutkan list (`sort`):
```python
angka = [3, 1, 4]; angka.sort()
```

## IX. Struktur Data: Tuple, Set, Dictionary
81. Membuat tuple:
```python
koordinat = (10, 20)
```
82. Mengakses tuple:
```python
x = koordinat[0]
```
83. Membuat set (himpunan unik):
```python
angka_unik = {1, 2, 2, 3}
```
84. Menambah elemen ke set (`add`):
```python
angka_unik.add(4)
```
85. Membuat dictionary (key-value):
```python
mhs = {"nama": "Ali", "umur": 21}
```
86. Mengakses value dictionary:
```python
nama = mhs["nama"]
```
87. Mengubah value dictionary:
```python
mhs["umur"] = 22
```
88. Menambah key-value baru ke dictionary:
```python
mhs["jurusan"] = "Informatika"
```
89. Menghapus key dari dictionary (`del`):
```python
del mhs["umur"]
```
90. Mengecek key di dictionary dengan `in`:
```python
ada = "nama" in mhs
```

## X. Fungsi Dasar (Functions)
91. Mendefinisikan fungsi tanpa parameter:
```python
def sapa():
    print("Halo!")
```
92. Memanggil fungsi:
```python
sapa()
```
93. Fungsi dengan satu parameter:
```python
def cetak_nama(nama):
    print(nama)
```
94. Fungsi dengan dua parameter:
```python
def tambah(a, b):
    return a + b
```
95. Menggunakan nilai kembalian (`return`):
```python
hasil = tambah(2, 3)
```
96. Fungsi dengan argumen default:
```python
def salam(pesan="Halo"):
    print(pesan)
```
97. Fungsi anonim (Lambda sederhana):
```python
kali = lambda x: x * 2
```
98. Menggunakan fungsi lambda:
```python
print(kali(5))
```
99. Fungsi dengan keyword arguments:
```python
def perkenalan(nama, hobi):
    print(nama, hobi)
perkenalan(hobi="Membaca", nama="Rina")
```
100. Fungsi mengembalikan banyak nilai sekaligus:
```python
def hitung(a, b):
    return a+b, a-b
tambah_res, kurang_res = hitung(5, 3)