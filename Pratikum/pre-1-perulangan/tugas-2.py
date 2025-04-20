jumlah_deret = int(input("Masukkan jumlah deret: ")) 
angka_range = range(1, jumlah_deret + 1)

for i in angka_range:
    print(f"i sekarang -> {i}")
    print(i * 2)
   