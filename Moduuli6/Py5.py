def poista_parittomat(luvut):
    return [luku for luku in luvut if luku % 2 == 0]

luvut = [2,5,3,5,4,1]
karsittu_lista = poista_parittomat(luvut)

print(f"alkuperäinen lista: {luvut}")
print(f"karsittu lista: {karsittu_lista}")