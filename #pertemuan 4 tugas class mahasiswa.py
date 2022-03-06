# ANDI RAHMATULLAH
# 5210411249

class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk,universitas):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk 
        self.__universitas = universitas

    def Tampil(self) :
        print(f"{self.nama} adalah mahasiswa {self.__universitas} prodi {self.prodi} dengan nim {self.nim}")


m1 = Mahasiswa("Udin", "10120371", "Sistem Informasi", 2020, "UTY")

teks = '{} adalah mahasiswa {} dengan nim {}'.format(m1.nama, m1.prodi, m1.nim)
print(teks)