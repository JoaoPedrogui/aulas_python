'''
print[0]
print[0:5]
'''
lista = [1,45,34,12,7,9,19,14,77]

'''
lista.sort()
lista.sort(reverse=True)
print(f"Lista ordenada{lista}")
'''
'''
lista.remove(12)
lista.pop(5)
del lista[2:5]
'''
'''
nome = "joao"
lista.append(nome)
print(lista)
'''
'''
# insercao
lista.incert(2,"lima")
print(lista)
'''
'''
# substituicao
lista[2] = "joao"
print[lista]
'''
'''
print("guimaraes" not in lista)
print("guimaraes" in lista)
'''
if "lima"  in lista:
    # esse bloco so sera exacutado quando a condicao é true
    print("sim, ele esta na lista")
else:
     # esse bloco so sera exacutado quando a condicao é false
    print("Não, o lima nao esta na lista")

NOTAS = []

print(20*"-", "BOLETIM ESCOLAR",20*"-")

numero_usuario1 = int(input("Digite uma nota: "))
notas.append(numero_usuario1)

numero_usuario2 = int(input("Digite uma nota: "))
nots.append(numero_usuario2)

numero_usuario3 = int(input("Digite uma nota: "))
nots.append(numero_usuario3)

numero_usuario4 = int(input("Digite uma nota: "))
nots.append(numero_usuario4)

numero_usuario5 = int(input("Digite uma nota: "))
nots.append(numero_usuario5)

# len conta a quantidade de elementod dentro de uma lista
quantidade_notas = len(notas)

# sum irá somar todos os valores da lista
soma = sum(notas)

media = soma / quantidade_notas

print(f"A notas são: {notas}")
print(f"A quantidade de notas: {quantidade_notas}")
print(f"A soma de todas ass notas: {soma_de_todas_notas}:")

'''
#TODO: Situação
