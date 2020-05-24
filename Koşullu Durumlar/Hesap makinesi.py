
while True:
    print("*********************************************"
          "\n1.işlem :toplama"
          "\n2.işlem :çıkarma"
          "\n3.işem :çarpma"
          "\n4işlem :bölme"
          "\n*********************************************")
    sayı1=int(input("1. sayı:"))
    sayı2=int(input("2. sayı:"))
    işlem=int(input("işlem:"))
    if işlem==1 :
        print("sonuç:{}".format(sayı1+sayı2))
    elif işlem==2 :
        print("sonuç:{}".format(sayı1-sayı2))
    elif işlem==3 :
        print("sonuç:{}".format(sayı1*sayı2))
    elif işlem==4 :
        print("sonuç:{}".format(sayı1/sayı2))
    else :
        print("Geçersiz işlem")

