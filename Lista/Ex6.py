valores = []
contagem = 0
while True:
    valores.append(int(input("Digite um número(digite 0 para parar): ")))
    contagem += 1
    if 0 in valores:
        valores.remove(0)
        break
valores.sort(reverse=True)
if 5 in valores:
    print("5 está na lista")
print(f"A lista de valores é: {valores} e a contagem de elementos é: {contagem-1}")
