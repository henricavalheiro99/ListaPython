num = [9, 7, 10, 4, 6, 3]
#num.sort()
num.sort(reverse= True)
soma = sum(num)
maior = max(num)
menor = min(num)
num2 = num[:]
num2[1] = 2
print(f"A lista é: {num} e a soma é: {soma}")
print(f"O maior é: {maior} e o menor é: {menor}")