# Meminta input nama dan umur jangan ytta pls kelempar ntar
print("jangan nulis ytta ya, admint marah")
name = input("whats ur name: ")

# Selama yang diketik adalah "ytta", jalankan perintah di dalam blok ini terus-menerus alias loop ya suki.
while name.lower() == "ytta":
    print("nulis yg bener!!!!")
    name = input("whats ur name: ") # Meminta input ulang sampai benar, jangan ngawur ya suki.
    
age = input("how old r u: ")

# Menyapa menggunakan f-string (ytta)
print(f"hello {name}!")

# Mengubah tipe data age dari string ke integer (angka) agar bisa dihitung 
age = int(age)
age = age + 1

#  hasil akhir
print("happy bday!")
print(f"youre {age} years old")

#masih satu keluarga di project "kakap" latihan user-input, f-string, dan type conversion dan jangan tanya gw gw juga ga paham 