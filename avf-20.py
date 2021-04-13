vetorPaciente = []
paciente = {}
print("Digite suas informações")
print("="*26)
for i in range(0,10):
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))
  print('-'*28)
  imc = peso / (altura*altura)
  imc = round(imc,2)
  paciente[nome] = {
        "nome": nome,
        "idade": idade,
        "peso":peso,
        "altura":altura,
        "imc": imc
  }
  vetorPaciente.append(paciente[nome])
print("Dados do paciente")
print("="*26)
for chave, valor in paciente.items():  
  print(f"Nome: {paciente[chave]['nome']}\nIdade: {paciente[chave]['idade']}\nPeso: {paciente[chave]['peso']}\nAltura: {paciente[chave]['altura']}\nIMC: {paciente[chave]['imc']}")
  print("-"*27)
