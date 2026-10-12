#input data 2 part 
nama_part1= input("\nmasukan nama part 1 : ")
uji_tekanan_part1 = int(input("masukan hasil uji tekanan (0-10 bar) : "))

nama_part2 = input("\nmasukan nama part 2 : ")
uji_tekanan_part2 = int(input("masukan hasil uji tekanan (0-10 bar) : "))

#proses perhitungan
jumlah_part = 2
makasimal_uji_tekanan = 10

persentase_part1 = (uji_tekanan_part1 / makasimal_uji_tekanan) * 100
persentase_part2 = (uji_tekanan_part2 / makasimal_uji_tekanan) * 100

total_skor_uji = uji_tekanan_part1 + uji_tekanan_part2
rata_rata = (total_skor_uji / (makasimal_uji_tekanan * jumlah_part)) * 100

#output
print("\n--- hasil uji tekanan mesin esspresso ---")
print(f"{nama_part1} : {persentase_part1}%")
print(f"{nama_part2} : {persentase_part2}%")
print(F"\nTotal skor uji : {total_skor_uji} bar")
print(F"{rata_rata:.2f}% rata-rata keLayakan : {rata_rata:.2f}%")
