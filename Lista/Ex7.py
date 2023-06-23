valores = []
while True:
    num = (int(input("Digite um valor: ")))
    if num in valores:
        valores.pop()
    valores.append(num)
    sair = str(input("Deseja sair?[S/N]: "))
    if sair == "S" or sair == "s":
        break
valores.sort()
print(valores)
