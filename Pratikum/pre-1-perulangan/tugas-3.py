jumlah = int(input("Masukkan jumlah deret Fibonacci: "))
a, b = 0, 1 # a = nilai pertama, b = nilai kedua

for i in range(jumlah):
    print(a, end= ", ")
    a, b = b, a + b # rumus fibonacci
