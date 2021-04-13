nome = input("Digite seu nome: ")
altura = int(input("Digite sua altura em centimetros:"))
sexo = input("Digite seu sexo: (Feminino/Masculino): ").lower()

if sexo == "feminino":
  if altura > 170:
    print("Sua estatura é: ALTA")
  elif altura > 159 and altura <= 170:
        print("Sua estatura é: MÉDIA")
  else:
    print("Sua estatura é: BAIXA")
else:
   if altura > 178:
    print("Sua estatura é: ALTA")
   elif altura > 165 and altura <= 178:
        print("Sua estatura é: MÉDIA")
   else:
        print("Sua estatura é: BAIXA")
