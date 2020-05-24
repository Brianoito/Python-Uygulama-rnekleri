"""ax^2+bx+c"""
print("ax^2+bx+c Şeklindeki deklem kökleri")
a=int(input("a Değeri:"))
b=int(input("b Değeri:"))
c=int(input("c değeri:"))
delta = (b**2)-(4*a*c)
if delta<=0 :
    print("reel kök yoktur")
else:
    kök1=(-b-delta**0.5)/(2*a)
    kök2=(-b+delta**0.5)/(2*a)
    print("1.kök:{}\n2.kök:{}".format(kök1,kök2))