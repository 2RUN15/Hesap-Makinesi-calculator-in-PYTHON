#Hesap Makinesinin alternatifidir
#Burda islemler yer alır
import time
def topla():
    #Burada sayılar toplanır
    girlen_sayilar = []
    while True:
        try:
            deger = int(input("Kaç sayı yazacaksın: "))
            break
        except ValueError:  
            print("Lütfen sayı giriniz")
    while True:
        try:
            sayi = int(input("Sayılar giriniz: "))
            girlen_sayilar.append(sayi)
            deger = deger-1
            if deger == 0:
                break
        except ValueError:
            print("Lütfen sayı girinz")  
    toplama = sum(girlen_sayilar)
    print(f"Girilen işlemin sonucu = {toplama}")

def carpım():
    #Burada sayılar çarpılır
    girlen_sayilar = []
    while True:
        try:
            deger = int(input("Kaç sayı yazacaksın: "))
            break
        except ValueError:
            print("Lütfen sayı giriniz")
    while True:
        try:
            sayi = int(input("Sayılar giriniz: "))
            girlen_sayilar.append(sayi)
            deger = deger-1
            if deger == 0:
                break
        except ValueError:
            print("Lütfen sayı girinz")  
    carp = 1
    for i in girlen_sayilar:
        carp *= i
    print(f"Girilen işlemin sonucu = {carp}")

def bolum():
    #Burada sayılar bölünür
    girlen_sayilar = []
    while True:
        try:
            deger = int(input("Kaç sayı yazacaksın: "))
            break
        except ValueError:
            print("Lütfen sayı giriniz")
    while True:
        try:
            sayi = int(input("Sayılar giriniz: "))
            girlen_sayilar.append(sayi)
            deger = deger-1
            if deger == 0:
                break
        except ValueError:
            print("Lütfen sayı girinz")
    try:
            
        sonuc = girlen_sayilar[0]
        girlen_sayilar.pop(0)
        for i in girlen_sayilar:
            sonuc /= i
        print(f"Girilen işlemin sonucu = {sonuc}")
    except ZeroDivisionError:
        print("Sayı sıfıra bölünmez")

def cikarma():
    #Burada sayılar çıkarılır
    girlen_sayilar = []
    while True:
        try:
            deger = int(input("Kaç sayı yazacaksın: "))
            break
        except ValueError:
            print("Lütfen sayı giriniz")
    while True:
        try:
            sayi = int(input("Sayılar giriniz: "))
            girlen_sayilar.append(sayi)
            deger = deger-1
            if deger == 0:
                break
        except ValueError:
            print("Lütfen sayı girinz")
    ilk_sayi = girlen_sayilar[0]
    geri_kalanlar = sum(girlen_sayilar) - ilk_sayi
    sonuc = ilk_sayi - geri_kalanlar

    print(f"Girilen işlemin sonucu = {sonuc} ")
    

def kare_kok():
    #Burada sayının karekökü alınır
    while True:
        try:
            sayi = int(input("Sayı giriniz: "))
            break
        except ValueError:
            print("Lütfen sayı giriniz")
    sonuc = sayi **0.5
    print(f"Girilen işlemin sonucu = {sonuc}")

def factoriel():
    #Burada sayının faktöriyeli alınır
    while True:
        try:
            sayi = int(input("Sayı giriniz: "))
            break
        except ValueError:
            print("Lütfen sayı giriniz")
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc *= i
    print(f"{sayi}! = {sonuc} ")

def asal_sayi():
    #Burada asal sayı bulunur
    bolen_liste = []
    while True:
        try:
            sayi = int(input("Sayı giriniz: "))
            break
        except ValueError:
            print("Lütfen sayı giriniz")
    for i in range(1,sayi+1):
        if sayi %i == 0:
            bolen_liste.append(i)
    tane = len(bolen_liste)
    if tane == 2:
        print(f"{sayi}'sayısı asaldır")
    else:
        print(f"{sayi}'sayısı asal değildir")
        