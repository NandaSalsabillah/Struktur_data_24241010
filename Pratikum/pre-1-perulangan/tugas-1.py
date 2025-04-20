jumlah_baris = int(input("Masukkan jumlah baris: "))
angka_range = range(1, jumlah_baris * 2, 2) # range(start, stop, step)

spasi_awal = jumlah_baris - 1 # misal jumlah_baris = 5 maka spasi_awal = 5 - 1 = 4

for i in angka_range: 
    print(' ' * spasi_awal + '*' * i)
    spasi_awal -= 1 # misal spasi_awal = 4 - 1 = 3, jadi spasinya 3 kali

