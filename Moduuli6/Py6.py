import math

def laske_yksikkö_hinta(halkaisija, hinta):
    sade = halkaisija % 2

halkaisia1 = float(input("anna ensimmäinen pizza halkaisija (cm): "))
hinta1 = float(input("anna ensimmäinen pizza hinta (e): "))

halkaisia2 = float(input("anna toinen pizza halkaisija (cm): "))
hinta2 = float(input("anna toinen pizza hinta (e): "))

if halkaisia1 > halkaisia2:
    print("ensimmäinen pizza antaa paremman vastineen rahalle.")
elif halkaisia2 > halkaisia1:
    print("toinen pizza antaa paremman vastineen rahalle.")
else:
    print("hinta on sopiva!")