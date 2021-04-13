paciente = {}
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura*altura)
imc = round(imc,2)
paciente[nome] = {
      "nome": nome,
      "idade": idade,
      "peso":peso,
      "altura":altura,
      "imc": imc
}
for chave, valor in paciente.items():
  print("Dados do paciente")
  print(f"Nome: {paciente[chave]['nome']}\nIdade: {paciente[chave]['idade']}\nPeso: {paciente[chave]['peso']}\nAltura: {paciente[chave]['altura']}\nIMC: {paciente[chave]['imc']}")
