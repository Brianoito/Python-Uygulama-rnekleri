def mük_sayı_kontrol(a):
    sonuç=0
    tambölenliste=[]
    for i in range(1,a):
        if a%i == 0:
            tambölenliste.append(i)#buraya kadar tam bölenleri bir listeye ekledik
    for i in tambölenliste:
        sonuç += i
    if sonuç==a:#tam bölenleri toplayıp mükemmel sayı olma koşulumuzu yazdık
        return print(".",sonuç)
while True:
    x=input("Kaça Kadar Olan Mükemmel Sayıları İstersiniz(çıkmak için q'ya basınız):")
    if x == "q":
        print("Programdan Çıkılıyor...")
        break
    for i in range(1,int(x)):
        mük_sayı_kontrol(i)