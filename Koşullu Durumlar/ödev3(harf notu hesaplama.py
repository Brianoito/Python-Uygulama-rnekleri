"""
    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""
print("NOT HESAPLAMA ARACI")
a=int(input("vize 1:"))
b=int(input("vize 2:"))
d=int(input("vize 3:"))
note=(3*a+3*a+4*a)/10
if note>=90 :
    print("Notunuz: AA")
elif note>=85 :
    print("Notunuz: BA")
elif note>=80 :
    print("Notunuz: BB")
elif note>=75 :
    print("Notunuz: CB")
elif note>=70 :
    print("Notunuz: CC")
elif note>=65 :
    print("Notunuz: DC")
elif note>=60 :
    print("Notunuz: DD")
elif note>=55 :
    print("Notunuz: FD")
elif note>=50 :
    print("Notunuz: FF")
else :
    print("Kaldınız!!!")

