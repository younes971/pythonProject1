import json

import requests

def hae_Chuck_Norris_vitsi():
    pyyntö = "https://api.chucknorris.io/jokes/random"
    try:
        vastaus = requests.get(pyyntö)
        vastaus.raise_for_status()
        json.vastaus = vastaus.json()
        print(json.vastaus["value"])
    except requests.exceptions.RequestException as e:
        print(f"haku ei voitu suorittaa!")

if __name__ == "__main__":
    hae_Chuck_Norris_vitsi()


