#5210411249
#ANDI RAHMATULLAH
#PBO-7 WEEK 5

#Single Inheritance

#Parent Class
class Hewan :   
    def bersuara(self) :
        print("Kucing Bersuara")
#5210411249
# Anak class mewarisi parent class
class Kucing(Hewan) :
    def suara(self) :
        print("miaw...miaw")
#5210411215

#Objek
cat = Kucing()
cat.suara()
cat.bersuara()

#5210411249
#ANDI RAHMATULLAH
#PBO-7 WEEK 5