#ANDI RAHMATULLAH
#5210411249

#Implementasi Overriding Class Segi Empat
class Segiempat() :
    def __init__(self, panjang, lebar) :
        self.panjang = panjang
        self.lebar = lebar
    #5210411249_ANDI RAHMATULLAH
    def hitungLuas(self) :
        print(f"Luas Segiempat : {self.panjang * self.lebar}")

class Bujursangkar(Segiempat) :
    def __init__(self,sisi) :
        self.side = sisi
        Segiempat.__init__(self, sisi, sisi)
    #5210411249_ANDI RAHMATULLAH

    #Overriding
    def hitungLuas(self) :
        print(f"Luas Bujur Sangkar = {self.side * self.side}")

b = Bujursangkar(4)
s = Segiempat(2, 4)
b.hitungLuas()#5210411249_ANDI RAHMATULLAH
s.hitungLuas()