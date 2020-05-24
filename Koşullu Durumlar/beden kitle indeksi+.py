print("Beden Kitle İndeksi Hesaplama Aracı")
boy=float(input("Boy(m):"))
kilo=float(input("Kilo(kg):"))
a=kilo/boy**2
print("Beden Kitle İndeksiniz: {}".format(kilo/boy**2))
if a <18.5 :
    print("Zayıfsınız")
elif 18.5<=a<=25 :
    print("Normalsiniz")
elif 25<a<=30 :
    print("Fazla Kilolarınız var")
else :
    print("Sağlığınız Tehlikede Obezsiniz")
