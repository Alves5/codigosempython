paciente = ["nome",0,0,0,0]
paciente[0] = input("Digite seu nome: ")
paciente[1] = int(input("Digite sua idade: "))
paciente[2] = float(input("Digite seu peso: "))
paciente[3] = float(input("Digite sua altura: "))
imc = paciente[2]/ (paciente[3]*paciente[3])
paciente[4] = round(imc,3)
print("Dados do paciente")
print("="*25)
print(f"Nome: {paciente[0]}\nIdade: {paciente[1]}\nPeso: {paciente[2]}\nAltura: {paciente[3]}\nIMC: {paciente[4]}")