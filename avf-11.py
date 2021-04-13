print("**** Exame de Doping ****")
print("="*25)
nome = input("Nome do atleta: ")
testosterona = int(input("Digite a testosteronado atleta: "))
if testosterona > 1400:
  print("Resultado: POSISTIVO.\nSua testosterona está acima de 1400.")
else:
  print("Resultado: NEGATIVO.")