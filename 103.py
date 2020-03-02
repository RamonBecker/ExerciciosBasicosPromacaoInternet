#!/usr/bin/python3

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}




book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'



# 1) Resolvido

titulo1 = book1.split(' by Yuval Noah Harari, 2015')
homoDeus = ' '.join(titulo1)
print(homoDeus)

titulo2 = book2.split(' by Nassim Nicholas Taleb, 2012')
antifragile = ' '.join(titulo2)
print(antifragile)

titulo3 = book3.split(' by Randomness by Nassim Nicholas Taleb, 2001')
fooled = ' '.join(titulo3)
print(fooled)

#2 Resolvido
'''
auxIndiceTitulo1 = book1[::].find('by')
auxIndiceTitulo2 = book2[::].find('by')
auxIndiceTitulo3 = book3[::].find('by')

auxTitulo1 = book1[:auxIndiceTitulo1 - 1]
auxTitulo2 = book2[:auxIndiceTitulo2 - 1]
auxTitulo3 = book3[:auxIndiceTitulo3 - 1]

print(auxTitulo1)
print(auxTitulo2)
print(auxTitulo3)


#3 

print(len(auxTitulo1))
print(len(auxTitulo2))
print(len(auxTitulo3))


#4 


def funcaoMensagemFormatada(book):

    titulo = book.split(' by ')

    for letra in titulo:
        titulo1 = letra.split(', ')

    titulo1.insert(0, titulo[0])
    msg = '{0} - {1} , {2}'.format(titulo1[0], titulo1[1], titulo1[2])
    print(msg)


funcaoMensagemFormatada(book1)
funcaoMensagemFormatada(book2)
funcaoMensagemFormatada(book3)

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'


def verificarPalindrome(string):
	auxString = string.replace(" ", "").lower()
	return auxString == auxString[::-1]
	
print(verificarPalindrome(palindrome_one.lower()))
print(verificarPalindrome(palindrome_two.lower()))
print(verificarPalindrome(palindrome_three.lower()))
print(verificarPalindrome(palindrome_four.lower()))'''