print("============Convetendo Moedas==============")
print("Qual o valor que deseja converter?")
valor_real = float(input())
print("Para qual a moeda deseja converter? Dólar(1), Euro(2), Libra(3)")
moeda = input()

#Recebimento de taxas
txdolar = 5.68
txeuro = 6.71
txlibra = 7.90
valor_final = 0.0
print("===========================================")
print("Valor R$", valor_real)
if moeda == "1":
    valor_final = valor_real / txdolar
    print("Valor U$",round(valor_final,2))
    print("Taxa:",txdolar)
elif moeda == "2":
    valor_final = valor_real / txeuro
    print("Valor €$",round(valor_final,2))
    print("Taxa:",txeuro)
elif moeda == "3":
    valor_final = valor_real / txlibra
    print("Valor £$",round(valor_final,2))
    print("Taxa:",txlibra)
else:
    print("Moeda não identificada, por favor tente novamente.")