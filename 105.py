#!/usr/bin/python3

#Desafio

lista = list(range(0,1000,2))


# Exercicio 1
lista = ['a','b','c']

tamanho = len(lista)

for i in range(tamanho): 
    lista[i] = lista[i].upper()

print(lista)



#Exercício 2

lista = [1,2,3,4,5]

#Outra forma de somar os elementos
#print(sum(lista))

aux = 0
tamanho = len(lista)
for i in range(tamanho):
   print(lista[i])
   aux += lista[i]

print("Soma dos elementos:", aux)



#Exercicio 3

lista = [1,2,3,4,5]
print(lista[::2])

#Exercicio 4


texto = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'


texto = texto[:].replace(",", "")
texto = texto[:].replace(".","")

auxTexto = texto.split(" ")

cont = 0
for i in auxTexto:
    if len(i) >= 5:
        cont += 1 


print('Qtd de palavras maiores que 5:',cont)

#Exercicio 5

lista = [i for i in range(1,100) if i % 3 == 0]
print(lista)

#Exercicio 5 b

lista = list((range(2,11)))
print(lista)


def encontrarPrimo(lista):
    aux = 0
    tamanhoLista= len(lista)
    for i in range(tamanhoLista):
        for j in range(0,tamanhoLista):
            if lista[i] % lista[j] == 0:
                aux += 1

        if(aux == 1):
            print("É primo", lista[i])
        aux = 0
                         

encontrarPrimo(lista)


