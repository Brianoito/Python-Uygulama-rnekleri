print("Faktöriyel Bulma Aracı")
while True :
    x=(input("Faktöriyelini Bulmak İstediğiniz Sayıyı Giriniz(çıkmak için 'q' ya basınız):"))
    if x=="q":
        break
    else:
        x=int(x)
        sonuç=1
        for i in range(1,x+1) :
            sonuç*=i
        print("Sonuç",sonuç)
        if x==0:
            print("Sonuç",1)
        elif x =="q" :
            break   