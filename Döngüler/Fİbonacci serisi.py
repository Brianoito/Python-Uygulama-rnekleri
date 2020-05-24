x=1
y=1
print("Fibonacci Bulma Aracı")
k=int(input("İlk Kaç Fibonaci Sayısını Bulmak İstersiniz:"))
a=[1,1]
for i in range(k-2):
    y=x+y
    x= y - x
    a.append(y)
print(a)
# YAPTIĞIN İŞLEM YERİNE BUNU YAPABİLİRSİN
# x,y=x,x+y 