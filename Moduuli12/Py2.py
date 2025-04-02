import requests

def hae_sää_tila(paikkakunta, api_avain):
    pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&lang=fi"
    paikkakunta = input("anna paikkakunnan nimi: ")
    try:
        vastaus = requests.get(pyyntö)
        vastaus.raise_for_status()
        json_vastaus = vastaus.json()

        lampotila_kelvin = json_vastaus["main"]["temp"]
        lampotila_celsius = lampotila_kelvin - 273.15

        print(f"Sää {paikkakunta}, lämpötila: {lampotila_celsius:.1f}°C")
    except requests.exceptions.RequestException as e:
        print("säätietoja ei voitu hakea:", e)