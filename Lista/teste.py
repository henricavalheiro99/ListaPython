num = []
while True:
    num.append(int(input("Digite um número: ")))
    saida = str(input("Deseja continuar[S/N]: "))
    if saida in "Nn":
        break
print(f"Os números são {num}")