import islemler
import time
def ilk_giris():
        global harf
        #Burası kullanıcıdan değer alma yeridir
        print("Hesap makinesi alternatifine hoş geldin kullanıcı")
        time.sleep(0.8)
        while True:
            harf = input("""
Toplam = "+"
Çıkarma = "-"
Çarpma = "*"
Bölme = "/"
Karekök alma = "s"
Faktöriyel alma = "f"
Asal Sayı alma = "a"
Yada isterseniz çıkmak içim 'q' basınız
Yukarıdaki belirtildiği gibi yazınız' """)
            
            if harf == "+":
                islemler.topla()
                break
            elif harf =="-":
                islemler.cikarma() 
                break
            elif harf == "*":
                islemler.carpım()
                break
            elif harf == "/":
                islemler.bolum()
                break
            elif harf == "s":
                islemler.kare_kok()
                break
            elif harf == "f":
                islemler.factoriel()
                break
            elif harf == "a":
                islemler.asal_sayi()
                break
            elif harf == "q":
                break
            else:
                print("Lütfen düzgün harf giriniz")

def sonraki_giris():
    #Burası kullanıcıdan ikinci bir değer alma yeridir
    while True:
        harf = input("""
Bir kez daha işlem yapmak için 'r' Çıkmak için 'q' """)
        if harf == "r":
            ilk_giris()
        elif harf == "q":
            break
        else:
            print("Lütfen düzgün harf giriniz")

ilk_giris()
while harf !="q":
    sonraki_giris()
    break                   
