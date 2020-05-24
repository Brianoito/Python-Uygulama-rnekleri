a = int(input("Kenar-1:"))
b = int(input("Kenar-2:"))
c = int(input("Kenar-3:"))
d = int(input("Kenar-4:"))

if (a == b and a == c and a == d):
    print("Kare")
elif (a == c and b == d):
    print("Dikdörtgen")
else:
    print("Dörtgen")