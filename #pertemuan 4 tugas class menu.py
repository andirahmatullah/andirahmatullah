# ANDI RAHMATULLAH
# 5210411249

class MenuMinuman:
    def __init__(self, nama, deskripsi, harga,stok):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__stok = stok

    def Tampil(self) :
        print(f"{self.nama} harga Rp {self.harga} \n---> {self.deskripsi} sisa stok {self.__stok}\n")


mnm1 = MenuMinuman("Jus Jambu", "Jus jambu merah tanpa gula", 8500, 12)
mnm2 = MenuMinuman("Jus Alpukat", "Jus alpukat dengan gula merah", 15000, 18)
mnm3 = MenuMinuman("Jus Alpukat Ektra Milk",
                   "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000,  25)
mnm4 = MenuMinuman(
    "Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500, 18)

pilihan_minuman = [mnm1, mnm2, mnm3, mnm4]
print("Daftar Menu Healty Fruits")
for mn in pilihan_minuman:
    t = '{} harga Rp {}, {}'. format(mn.nama, mn.harga, mn.deskripsi)
    print(t)