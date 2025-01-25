
tuumamäärä = 1
while tuumamäärä >= 0:

        tuumamäärä = int(input("anna tuumamäärä, jos on negatiivinen arvo ohjelma lopetetaan: "))
        if tuumamäärä < 0:
            print("negatiivinen arvo, ohjelma lopetetaan.")
        else:
            senttimetrit = tuumamäärä * 2.54
            print(f"{tuumamäärä}, tuuma on {senttimetrit:.2f} cm.")












