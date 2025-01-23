
vuosiluku = int(input("anna vuosiluku: "))

if vuosiluku % 400 == 0:
    print("vuosi on karkausvuosi.")
elif vuosiluku  % 100 == 0:
    print("vuosi ei ole karkausvuosi.")
elif vuosiluku % 4 == 0:
    print("vuosi on karkausvuosi.")
else:
    print(f"vuosi ei ole karkausvuosi.")


