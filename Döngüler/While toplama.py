toplam=0
while True:
    x=input("Toplayacağınız Sayıları Girin(sonucu görmek için \"q\" ya basın:")
    if x=="q":
        print("Toplam:",toplam)
    else:
        toplam+=float(x)
