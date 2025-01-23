
hyttiluokka = input("anna hyttiluokka: ")

LUX = "arvekkeellinen hytti yläkanella"
A = "ikkunallinen hytti autokannen yläpuolella"
B = "ikkunaton hytti autokannen yläpuolella"
C = "ikkunaton hytti autokannen alapuolella"

if hyttiluokka == "LUX":
    print("LUX on parveekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen alapuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

