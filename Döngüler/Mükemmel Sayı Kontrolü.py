print("Kendisi Hariç Tüm Çarpalarının Toplamı Kendisine Eşit Olan Sayıya Mükemmel Sayı Denir")
while True:
    girdi=int(input("Mükemmel Sayı Kontrolü:"))
    çarpanliste=list(range(1,girdi+1))
    x=[]
    sonuç=0
    for i in çarpanliste :
        y=girdi/i
        if girdi%i == 0 :
            x.append(y)
    for i in x :
        sonuç+=i
    if (sonuç-girdi)==girdi :
        print("mükemmel sayı")
    else:
        print("mükemmel sayı değil")
