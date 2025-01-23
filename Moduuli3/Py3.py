
biologisen_sukupuoli = input("anna sukupuoli (mies/nainen): ")

hemoglobiini_arvo = float(input("anna hemoglobiini_arvot (g/l): "))

if biologisen_sukupuoli == "mies":
    if  hemoglobiini_arvo<134:
        print("hemoglobiini_arvo on alhainen.")
    elif hemoglobiini_arvo>195:
        print("hemoglobiini_arvo on korkea.")
    elif 134<= hemoglobiini_arvo <195:
        print("hemoglobiini_arvo on normaali.")

if biologisen_sukupuoli == "nainen":
    if hemoglobiini_arvo < 117:
        print("hemoglobiini_arvo on alhainen.")
    elif 117<= hemoglobiini_arvo <175:
        print("hemoglobiini_arvo on normaali.")
    else:
        print("hemoglobiini_arvo on korkea.")



