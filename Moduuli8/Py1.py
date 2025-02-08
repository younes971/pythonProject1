import sqlite3

def hae_lentoasema(icao_koodi):
    conn = sqlite3.connect("lentokentät")
    cursor = conn.cursor()

    cursor.execute("select name from airport")
    tulos = cursor.fetchall()

    if (tulos):
        print(f"lentoasema: tulos: {tulos}")

    else:
        print("lentoaema ei löytynyt")

    icao_koodi = input("anna lentoaseman ICAO-koodi: ")




