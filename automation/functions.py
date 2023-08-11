# QUESTION 1
def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):
    tam_bolunenler = []
    for sayi in range(min_sayi, max_sayi + 1):
        if sayi % bolen_sayi == 0:
            tam_bolunenler.append(sayi)

    return tam_bolunenler, len(tam_bolunenler)

# Deneme
print(bolunen_sayi_bulma(10, 20, 2))


# QUESTION 2
def sayi_okunusu(sayi):
    birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

    birinci_basamak = sayi % 10
    ikinci_basamak = sayi // 10

    if sayi < 10:
        return birler[sayi]
    elif sayi >= 10 and sayi <= 99:
        if birinci_basamak == 0:
            return onlar[ikinci_basamak]
        else:
            return onlar[ikinci_basamak] + " " + birler[birinci_basamak]


def sayi_atama(sayi):

    if sayi >= 10 and sayi <= 99:
        okunus = sayi_okunusu(sayi)
        print("Girilen sayı:", sayi)
        print("Okunuşu:", okunus)
    else:
        print("Lütfen 2 basamaklı bir sayı giriniz.")


girilen_sayi = int(input("Lütfen 2 basamaklı bir sayı giriniz: "))
sayi_atama(girilen_sayi)


# QUESTION 3
def harf_notu_hesapla(vize1, vize2, final):

    if vize1 < 0 or vize1 > 100 or vize2 < 0 or vize2 > 100 or final < 0 or final > 100:
        return "Geçersiz not girişi!"

    toplam_not = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)

    if toplam_not >= 90:
        return "AA"
    elif toplam_not >= 85:
        return "BA"
    elif toplam_not >= 80:
        return "BB"
    elif toplam_not >= 75:
        return "CB"
    elif toplam_not >= 70:
        return "CC"
    elif toplam_not >= 65:
        return "DC"
    elif toplam_not >= 60:
        return "DD"
    elif toplam_not >= 55:
        return "FD"
    else:
        return "FF"


girilen_vize1 = float(input("1. Vize  notunu giriniz: "))
girilen_vize2 = float(input("2. Vize  notunu giriniz: "))
girilen_final = float(input("Final notunu giriniz: "))

harf_notu = harf_notu_hesapla(girilen_vize1, girilen_vize2, girilen_final)

print("Harf Notu:", harf_notu)
