num = []
multiplicacao = 1
while True:
    num.append(int(input("Digite um número(digite 0 para parar): ")))
    if 0 in num:
        num.remove(0)
        break
maior = max(num)
menor = min(num)
soma = sum(num)
for i in num:
    multiplicacao *= i
print(f"A soma é: {soma}")
print(f"A multiplicação é: {multiplicacao}")
print(f"O maior é: {maior}")
print(f"O menor é: {menor}")