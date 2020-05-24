b=int(input("Kaça Kadar 3'e Bölünen Pozitif Sayıları İstiyorsunuz:"))
a=list(range(1,101))
for i in a:
    if i % 3!=0:
        continue
    print(i)
