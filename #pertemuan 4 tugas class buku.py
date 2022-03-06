# ANDI RAHMATULLAH
# 5210411249

class Buku:
    def __init__(self, judul, pengarang, tahun_terbit,jmlh_halaman):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__jmlh_halaman = jmlh_halaman

    def Tampil(self) :
        print(f"Buku {self.judul} karangan {self.pengarang} pertama kali diterbitkan tahun {self.tahun_terbit}")
        print(f"Buku {self.judul} jumlah halamannya adalah {self.__jmlh_halaman}\n")


buku = Buku('Tenggelamnya Kapal Van der Wijck', 'HAMKA', 1938,  125)
t = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(
    buku.judul, buku.pengarang, buku.tahun_terbit)
print(t)