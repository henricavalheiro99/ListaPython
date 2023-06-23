fruta = ["Maçã", "Banana", "Abacaxi", "Uva"]
fruta[3] = "Melancia"
fruta.append("Laranja")
fruta.insert(0, "Morango")
del fruta[3]
fruta.pop(2)
fruta.remove("Morango")
fruta.pop()
fruta.insert(0,"Abacaxi")
if "Abacaxi" in fruta:
    fruta.remove("Abacaxi")
else:
    print("Não encontrado")
maior = max(fruta)
menor = min(fruta)
print(fruta)
print(maior)
print(menor)
