print("GEOMETRİK ŞEKİL TÜRÜ BULMA ARACI")
while  True:
    a=int(input("Şekliniz Üçgense 3'e Basınız Dörgense 4'e "))
    if a==4:
        k1 = int(input("1.kenar:"))
        k2 = int(input("2.kenar:"))
        k3 = int(input("3.kenar:"))
        k4 = int(input("4.kenar:"))
        if k1==k2==k3==k4:
            print("Kare")
        elif (k1 == k2 or k1 == k3 or k1 == k4) and (k2 == k3 or k2 == k4 or k3 == k4) :
            print("Dik Dörtgen")
        else:
            print("Çeşit Kenar Dörtgen")
    elif a==3 :
        k1 = int(input("1.kenar:"))
        k2 = int(input("2.kenar:"))
        k3 = int(input("3.kenar:"))
        if abs(k1-k2)<k3<(k1+k2) and abs(k2-k3)<k1<(k2+k3) and abs(k3-k1)<k2<(k3+k1) :
            if k1==k2==k3 :
                print("Eş Kenar Üçgen")
            elif k1==k2 or k1==k3 or k2==k3 :
                print("İkiz Kenar Üçgen")
            else:
                print("Çeşit Kenar Ügen")

        else:
            print("Girdiğiniz Değerler Üçgen Belirtmez")
    else:
        print("Yanlış Bir Komut Girdiniz")
