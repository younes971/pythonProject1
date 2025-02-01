def gallonat_litroiksi(gallonmäärä):
    return gallonmäärä *  3.785

while True:
    gallonamäärä = float(input("anna gallonanmäärä litroiksi, lopeta jos negatiivinen luku: "))
    break
if gallonamäärä < 0:
        print("Lopeta!")

litrat = gallonat_litroiksi(gallonamäärä)
print(f"{gallonamäärä} gallona on {litrat:.2f} litraa.")

