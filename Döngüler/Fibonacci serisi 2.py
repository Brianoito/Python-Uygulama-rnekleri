liste = [1,1]
while True:
    print("Fibonacci Bulma Aracı")
    k=int(input("İlk Kaç Fibonaci Sayısını Bulmak İstersiniz:"))
    for i in range(10):
        liste.append(liste[-1] + liste[-2])
    print(liste)