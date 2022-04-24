isler = []
zamanlar = []

class Todo():


    def __init__ (self):
        global isler, zamanlar
        yapicalak = isler.append("kod yazılacak")
        zaman =     zamanlar.append("pazartesi")
    def ekle(self, yapilacak, zaman):
        self.yapilacak = isler
        self.zaman = zaman
        return isler.append(input("is giriniz: ")), zamanlar.append(input("yapılacak zamanı giriniz : "))
            
ayriyeten = Todo()
print("is {0}, su zaman {1}".format(isler, zamanlar))
print("ayriyeten: ")

ayriyeten.ekle(isler, zamanlar)
print(isler,zamanlar)