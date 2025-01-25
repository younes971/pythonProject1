
import math
numbers = []

user_input = input("syötä luvut yksi kerrallaan (lopeta painamalla E): ")

if user_input == "":
    print("virheelinen syötö, yritä uudelleen.")
    number = int(user_input)
    numbers.append(number)

if numbers:
    pienimmän = min(numbers)
    suurimman = max(numbers)
    print(f"pienin luku: {pienimmän}")
    print(f"suurin luku: {suurimman}")

else:
    print("!tarkista!")
