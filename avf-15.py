salarioF = []
for i in range(0,90):
  sal = float(input("Digite seu salario: "))
  salarioF.append(sal)
contagem = 0
for i in salarioF:
  if i < 900:
    contagem += 1
print(f"Funcionários que recebem abaixo de 900: {contagem}")
