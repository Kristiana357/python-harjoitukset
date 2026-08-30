vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0:
    print("Karkausvuosi")
elif vuosi % 100 == 0:
    print("Ei ole karkausvuosi")
elif vuosi % 4 == 0:
    print("Karkausvuosi")
else:
    print("Ei ole karkausvuosi")
