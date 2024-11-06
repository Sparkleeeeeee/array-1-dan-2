angka = []

for i in range(5):
    elemen = int(input(f"masukan angka ke-{i+1}:"))
    angka.append(elemen)

angka.sort()

print(f"array yang sudah diurutkan: {angka}")


