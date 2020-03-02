#!/usr/bin/python3


# 1 QUESTÃO

def verificarListasIguais(lista1, lista2):
	
	if(len(lista1) != len(lista1)):
		return False

	sizeLista = len(lista1)
	print(sizeLista)
	aux = 0

	for i in range(sizeLista):
		if(lista1[i] == lista2[i]):
			aux += 2

	somaTamanhoListas = len(lista1) + len(lista2)
	if somaTamanhoListas == aux:
         return True
    
	return False



lista1 = [1,2,3,4]
lista2 = [1,2,3,4]


# 2 QUESTÃO

print(verificarListasIguais(lista1, lista2))


palavra1 = input("Digite uma palavra:")
palavra2 = input("Digite uma segunda palavra:")

def verificarPalavrasPalindromes(palavra1, palavra2):
	if len(palavra1) != len(palavra2):
		return False

	auxPalavra1 = palavra1.replace(" ", "").lower()
	auxPalavra2 = palavra2.replace(" ", "").lower()

	if auxPalavra1 == auxPalavra1[::-1]:
		if auxPalavra2 == auxPalavra2[::-1]:
			return True

	return False

if verificarPalavrasPalindromes(palavra1, palavra2):
	print("As duas palavras são palindromes")
else:
	print("As duas palavras não são palindromes")