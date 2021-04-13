maiorNome = ""
cont = 0
for i in range(0,10):
  func = input(f"Digite o nome do {i+1}: ")
  if len(func) > cont:
    cont = len(func)
    maiorNome = func
print(maiorNome)