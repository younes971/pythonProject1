pituus_min = 37

kuhan_pituus = float(input(("anna kuhanpituus senttimetreinä: ")))
puuttuu = pituus_min - kuhan_pituus

if kuhan_pituus>=37:
    print(f"kuha täyttää ehdot, voit pidä sen.")

if kuhan_pituus<37:
    print(f"kuha on alamittainen, laske kuha takaisin järveen. kuha on {puuttuu:.1f} cm lyhyt")