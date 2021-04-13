somaP = 0
somaI = 0
for e in range(1,101):
  if e % 2 == 0:
    somaP += e
  else:
    somaI += e
print(f"Soma dos números pares: {somaP}\nSoma dos números ímpares: {somaI}")