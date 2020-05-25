def tamböl(a):
    tamböllist=[]
    for i in range(1,a+1):
        if a%i == 0:
            tamböllist.append(i)
    return tamböllist

while True:
    x = input("Tam Bölenleri Bulunacak Sayı(çıkmak için q'ya basınız):")
    if x == "q":
        print("Programdan Çıkılıyor...")
        break
    else:
        print(tamböl(int(x)))
        y = input("Bu sayılarla hangi işlemi yapmak istersiz(ana menüye gitmek için q'ya basınız "
                  "\n1.çarpma"
                  "\n2.toplama"
                  "\n")

        if y == "q":
            continue
        if int(y) == 1:
            sonuçç = 1
            for i in tamböl(int(x)):
                sonuçç *= i
            print("Sonuç", sonuçç)

        elif int(y) == 2:
            sonuçt = 0
            for i in tamböl(int(x)):
                sonuçt += i
            print("Sonuç", sonuçt)





