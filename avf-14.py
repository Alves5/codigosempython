number = int(input("Digite um número: "))
c = 0
for i in range(number,1,-1):
    c = i - 1
    number = (number * c)
print(number)