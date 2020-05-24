a=list(range(1,11))

for i in a:
    if i==6 or i==9 or i==10:
        print("**************************\n{}'lar\n**************************".format(i))
    else:
        print("**************************\n{}'ler\n**************************".format(i))
    for j in a :
       print("{}x{}={}".format(i,j,j * i))