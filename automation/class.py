# QUESTION 1

class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif


class Soru:
    def net_sayisi(self, dogru, yanlis):
        net = dogru - (yanlis / 4)
        return max(0, net)

    def hesapla(self, net):
        puan = net * 2
        return puan


girilen_ogrenci_adi = input("Öğrenci adını giriniz: ")
girilen_ogrenci_soyadi = input("Öğrenci soyadını giriniz: ")
girilen_ogrenci_sinif = input("Öğrenci sınıfını giriniz: ")


dogru_sayisi = int(input("Doğru sayısını giriniz: "))
yanlis_sayisi = int(input("Yanlış sayısını giriniz: "))


ogrenci = Ogrenci(girilen_ogrenci_adi, girilen_ogrenci_soyadi, girilen_ogrenci_sinif)
soru = Soru()


hesaplanan_net = soru.net_sayisi(dogru_sayisi, yanlis_sayisi)


hesaplanan_puan = soru.hesapla(hesaplanan_net)

print("Öğrenci Adı:", ogrenci.ogrenci_adi)
print("Öğrenci Soyadı:", ogrenci.ogrenci_soyadi)
print("Öğrenci Sınıfı:", ogrenci.ogrenci_sinif)
print("Net Sayısı:", hesaplanan_net)
print("Puan:", hesaplanan_puan)


# QUESTION 2

class Insan:
    def __init__(self, ad="Bilgi Yok", soyad="Bilgi Yok", yas=0, ulke="Bilgi Yok", sehir="Bilgi Yok"):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nYaş: {self.yas}\nÜlke: {self.ulke}\nŞehir: {self.sehir}\nYetenekler: {', '.join(self.yetenekler)}"

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


kisi = Insan(ad="Ahmet", soyad="Yılmaz", yas=30, ulke="Türkiye", sehir="Ankara")

kisi.yetenek_ekle("Bisiklete Binmek")
kisi.yetenek_ekle("Python Programlama")

print(kisi.kisi_bilgileri())
