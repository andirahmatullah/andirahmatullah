#ANDI RAHMATULLAH 
#5210411249
class Menu :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

minuman1 = Menu("Jus buah naga", "Jus buah naga merah tanpa gula", 8500)
minuman2 = Menu("Jus anggur", "Jus anggur dengan gula merah", 15000)
minuman3 = Menu("Jus apel", "Jus apel campuran susu cokelat dan tapuran kepingan choco", 15000)
minuman4 = Menu("Redvelvet", "Smoothie pisang susu dengan strawberry", 17500)

makanan1 = Menu("Mie dok dok", "Mie dok dok dengan telur", 12000)
makanan2 = Menu("Kerang Dara", "Kerang manis", 25000)
makanan3 = Menu("Nasi Goreng", "Nasi Goreng dengan telur setengah matang", 8000)
makanan4 = Menu("Tempe Geprek", "Tempe geprek sambel", 10000)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}'. format(makan.nama, makan.harga, makan.deskripsi)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}'. format(minum.nama, minum.harga, minum.deskripsi)
    print(teks)
print("\n")

class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswaA = Mahasiswa("Ahmad zaid", "5210411013", "Informatika")
mahasiswaB = Mahasiswa("jhosua", "5210411012", "Informatika")
mahasiswaC = Mahasiswa("ilham", "5210411248", "Informatika")
mahasiswaD = Mahasiswa("taufiq", "5210411034", "Informatika")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("List Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("Arah langkah", "fiersa basari", 2018)
buku2 = Buku("Definitely love", "ayu riana", 2020)
buku3 = Buku("Episode rasa", "suci indrayanti", 2020)

bukus = [buku1, buku2, buku3]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")