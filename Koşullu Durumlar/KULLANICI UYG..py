defid ="Brianoito"
defpassword ="123456"

id = input("İD:")
password = input("PASSWORD:")
while True :
    if ((defid == id) and (defpassword == password)):

        print("\nPROFİLE GİRİŞ YAPTINIZ")
        print("\nhttps://www.facebook.com/ibrahimm.ii")
        print("(linki kopyalayıp tarayıcıya yapıştırın)")
    elif ((defid == id) and (defpassword != password)):
        print("\nŞİFRE YANLIŞ!")

    else :
        print("\nKULLANICI BULUNAMADI!")