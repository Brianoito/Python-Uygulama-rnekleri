print("Armstrong Sayısı Kontrolü\nBir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya 'Armstrong' sayısı denir.")

sonuç=0
while True:
    x = int(input("Bir Sayı Girin:"))
    for i in str(x):
        sonuç += int(i) ** len(str(x))
    print("Sonuç:",sonuç)
    if sonuç == x:
        print("Armstrong Sayısı")
    elif sonuç !=x:
        print("Armstrong Sayısı Değil")
