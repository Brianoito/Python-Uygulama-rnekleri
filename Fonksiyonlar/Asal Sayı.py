def asalsayı(a):
    if a==2:
        return True
    elif a<=1:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                return False
        return True



while True:
    x = input("Asal Sayı Kontrolü(çıkmak için q'ya basınız):")
    if x == "q":
        print("Programdan Çıkılıyor...")
        break
    x = int(x)
    if asalsayı(x):
        print(x, "ASAL SAYIDIR")
    else :
        print(x, "ASAL SAYI DEĞİLDİR")

