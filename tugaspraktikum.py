#soal no 1

#int
a = 10           
#string       
b = "Halo"
#list       
d = [1, 2, 3]     

#menampilkan menggunakan fungsi type()  
print(type(a))
print(type(b))
print(type(d))

#soal no 2

belanja = ["beras", "minyak", "telur"]


belanja.append("gula")
belanja.append("kopi")


for item in belanja:
    print(item)
    
#soal no 3

harga = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

total = sum(harga.values())
print("Total harga belanjaan:", total)

#soal no 4
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return panjang ==10 , lebar ==5, luas, keliling

#soal no 5

usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia > 50:
    print("Lansia")
else:
    print("Usia tidak valid")
    



