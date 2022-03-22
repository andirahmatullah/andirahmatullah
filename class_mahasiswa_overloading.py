#ANDI RAHMATULLAH
#5210411249

#Implementasi Overloading Class Mahasiswa
class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
    #5210411249_ANDI RAHMATULLAH
    def tampilMhs(self) :
        print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}")

    #Method Overloading
    def hitungSks(self, jmlhsks = None, sks = None) :
        if jmlhsks != None and sks != None :
            totalsks = jmlhsks + sks#5210411249_ANDI RAHMATULLAH
            print(f"Total sks\t: {totalsks}")
        else :
            totalsks = jmlhsks#5210411249_ANDI RAHMATULLAH
            print(f"Total Sks\t: {totalsks}")

        if totalsks>=100 :#5210411249_ANDI RAHMATULLAH
            print("Diperbolehkan mengambil skripsi")
        else :
            print("Tidak diperbolehkan mengambil skripsi")
#5210411249_ANDI RAHMATULLAH
mahasiswa1 = Mahasiswa("Elan", 123180015)
mahasiswa2 = Mahasiswa("Mika", 123190007)

mahasiswa1.tampilMhs()
mahasiswa1.hitungSks(80, 34)
#5210411249_ANDI RAHMATULLAH
mahasiswa2.tampilMhs()
mahasiswa2.hitungSks(83)