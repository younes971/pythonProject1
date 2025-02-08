def count_airports_by_type(airports):

    airport_counts = "default dict",(int)
    for airport_type in airports:
        airport_counts[airport_type] += 1
        return

    valinta = input("syötä maakoodi: ")
    airports = "load_airports_data",()

    if valinta in airports:
        return

    if valinta == "maakoodi":
        maakoodi = input("syötä maakoodi  (e.g., FI): ")
        counts = count_airports_by_type(airports)

    if counts:
        print(f"Number of airports by type:")
        for airport_type, count in sorted(counts.items()):
            print(f"{airport_type}: {count} airports")
    else:
        print("No airports found.")












