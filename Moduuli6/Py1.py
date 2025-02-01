import random

def heitä_noppaa():
    return random.randint(1,6)

while True:
        silmaluku = heitä_noppaa()
        print(f"heitä noppaa: {silmaluku}")

        if silmaluku == 6:
            print("Onnea!")
            break