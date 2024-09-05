contador = 0
soma = 0
for i in range(0,101):
    if i % 2 != 0:
        print(i)
        contador +=1
        soma += i

print('A soma dos numeros impares é: {soma}')
print('A quantidade total de numeros impares é: {contador}')


