valores = []
while True:
    valores.append(int(input("Digite um número: ")))
    confirma = str(input("Deseja continuar?[S/N]: "))
    if confirma in "Nn":
        break
soma = sum(valores)
maior = max(valores)
print(f"A soma é: {soma} e o maior é: {maior}")