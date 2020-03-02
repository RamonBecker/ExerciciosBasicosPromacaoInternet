

from sys import getsizeof

#Exercício 1
#help(list)
#help(tuple)

#Exercicio 3

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

professor3 = dict(id=28, name='Jorge Armino', idade=37)

professor1['coordenadas'] = (24.0814, -44.8384)

professor2['coordenadas'] = (-81.4016, -113.3658)  

professor3['coordenadas'] = (36.5177, 135.8423)

#Exercicio 3
def diferencaTuplaLista(n):

    exemplo = []

    print("Lista com ", n)

    tamanhoListaArmazena = 0
    for number in range(n):
        exemplo.append(number)
        tamanhoListaArmazena =  getsizeof(exemplo)

    print("Tamanho de armazenamento em memória em:", tamanhoListaArmazena, ' bytes')


    print("Tupla com ", n)

    tamanhoTuplaArmazena = 0

    for number in range(n):
        exemplo = tuple(range(number))
        tamanhoTuplaArmazena = getsizeof(exemplo)
    print("Tamanho de armazenamento em memória em:", tamanhoTuplaArmazena, ' bytes')

diferencaTuplaLista(20)