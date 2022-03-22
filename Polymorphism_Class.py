#ANDI RAHMATULLAH
#5210411249

#Polymorphism dengan Class
class kucing :
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur
    #5210411249_ANDI RAHMATULLAH
    def bersuara(self) :
        print("Meow")

class dog :#5210411249_ANDI RAHMATULLAH
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur
    #5210411249_ANDI RAHMATULLAH
    def bersuara(self) :
        print("Guk...Guk...")

kucing1 = kucing("Tom", 3)
anjing1 = dog("Spike", 4)
#5210411249_ANDI RAHMATULLAH
for hewan in (kucing1, anjing1) :
    hewan.bersuara()