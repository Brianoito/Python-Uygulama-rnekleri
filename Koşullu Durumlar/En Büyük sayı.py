print("Hangi Sayı Daha Büyük Bulalım")
a=int(input("sayı 1:"))
b=int(input("sayı 2:"))
d=int(input("sayı 3:"))
if a>d and a>b:
    print("En Büyük Sayı{}".format(a))
elif b>d and b>a:
    print("En Büyük Sayı{}".format(b))
elif d>a and d>b:
    print("En Büyük Sayı{}".format(d))
