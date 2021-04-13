time = [[0,0,0,0,0],[0,0,0,0,0]]
soma = [0,0]
for i in range(0,2):
  for j in range(0,5):
    time[i][j] = float(input("Digite o salario: "))
    soma[i] += time[i][j]
print("Time titular")
print(f"Soma dos salários: {soma[0]}")
print(f"Média dos salários: {soma[0]/5}")
print("Time reserva")
print(f"Soma dos salários: {soma[1]}")
print(f"Média dos salários: {soma[1]/5}")