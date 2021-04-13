print("============Categoria Esportiva==============")
print("Qual o nome do atleta?")
nome = input()
print("Qual a idade do atleta?")
idade = int(input())
if idade >= 11 and idade <= 13:
    print("Categoria: Juvenil 1")
elif 14 <= idade <= 17:
    print("Categoria: Juvenil 2")
elif idade >= 18:
    print("Categoria: Adulto")
else:
    print("Você ainda é muito jovem, tente no próximo ano.")