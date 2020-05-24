print("Beden Kitle İndeksi Hesaplama Aracı")
boy=float(input("Boy(m):"))
kilo=float(input("Kilo(kg):"))
a=kilo/boy**2
print("Beden Kitle İndeksiniz: {}".format(kilo/boy**2))
if a <18.5 :
    print("Zayıf")
elif 18.5<=a<=25 :
    print("Normal")
elif 25<a<=30 :
    print("Fazla Kilolu")
else :
    print("obez")