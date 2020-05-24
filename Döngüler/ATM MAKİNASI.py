print("********************\nATM sistemine hoşgeldiniz\n********************")
bakiye=3000
while True:
    print("""
    İşlemler:
    
    1. Bakiye Sorgulama
    2. Para Yatırma
    3. Para Çekme
    
    Programdan 'q' tuşu ile çıkabilirsiniz.
    
    """)
    a=input("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ:")
    if a=="1" :
        print("Bakiye:",bakiye)
        input("ANA MENÜYE DÖNMEK İÇİN ENTER'A BASINIZ")
    elif a=="2" :
        yp=int(input("YATIRMAK İSTEDİĞİNİZ TUTARI GİRİNİZ:"))
        print("PARANIZ YATIRILIYOR...")
        bakiye+=yp
        print("YENİ BAKİYE:", bakiye)
        input("ANA MENÜYE DÖNMEK İÇİN ENTER'A BASINIZ")
    elif a=="3" :
        print("ÇEKİLEBİLİR TUTAR:",bakiye)
        çp=int(input("ÇEKMEK İSTEDİĞİNİZ TUTARI GİRİNİZ:"))
        bakiye-=çp
        print("PARANIZ VERİLİYOR...")
        print("YENİ BAKİYE:", bakiye)
        input("ANA MENÜYE DÖNMEK İÇİN ENTER'A BASINIZ")
    elif a=="q" or a=="Q" :
        print("İYİ GÜNLER DİLERİZ...")
        break
    else:
        print("HATALI TUŞLAMA YAPTINIZ")
        input("ANA MENÜYE DÖNMEK İÇİN ENTER'A BASINIZ")