#!/usr/bin/python
print("Exemplo de listas")

lista = ["valor1", "valor2", "val3"]

print(lista[1])
print(lista[2])

lista.append("valor4")

print(lista[3])

lista.remove("valor4")

# print(lista[3])
print(lista)
lista.reverse()
print(lista)


# const array know has tuples
arr = ("var1", "var2", "var3")
print(arr)
print(arr[1])

# multi assign
var1, var2, var3 = arr
print(var1)

tupla = tuple(lista)
print(tupla)

lista = list(tupla)
print(lista)


meuArr = ["valorA"]
# erro: mauArr[1] = "valorB"

print(meuArr)


# dicionario {}
dici = {}
dici["1"] = "valorB"

print(dici)
