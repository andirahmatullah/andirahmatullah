#5210411249
#ANDI RAHMATULLAH
#PBO-7 WEEK 5

#Multiple Inheritance

#Parent Class 1
class Perhitungan1 :
    def penjumlahan(self, a, b) :
        return a + b
#5210411249
#Parent Class 2
class Perhitungan2 :
    def perkalian(self, a, b) :
        return a * b    

#Anak Class
class Hitung(Perhitungan1, Perhitungan2) :
    def pembagian(self, a, b):
        return a / b    
#5210411249
#Objek
h = Hitung()    
print(h.penjumlahan(20, 20))
print(h.perkalian(5, 4))
print(h.pembagian(6, 12))

#5210411249
#ANDI RAHMATULLAH
#PBO-7 WEEK 5