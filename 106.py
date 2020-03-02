
import csv
from io import StringIO


#Exercício 1

def define_default_city(state):

    with open('capitais-BR.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=';')
        for linha in reader:
            if(linha[0].lower() == state.lower()):
                print(linha[1])
        else:
            print("Estado incorreto, não foi possível encontrar a cidade")
        
     

define_default_city("ac")


#Exercicio 2


buffer = StringIO()
estados_sudestes = ['São Paulo', 'Minas Gerais', 'Espírito Santo', 'Rio de Janeiro']
lista = []
armazenaPosicao = ['']
with open('capitais-BR.csv','r', encoding = 'utf-8') as csvfile:
        for index, line in enumerate(csvfile):
            lista = line.split(";")
            for i in estados_sudestes:
                if(i == lista[0]):
                   armazenaPosicao[0] = index
            buffer.write(' \n' if index == armazenaPosicao[0] else line)
        
with open('capitais-BR.csv', 'w', encoding = 'utf-8') as csvfile:
    csvfile.write(buffer.getvalue())

  
#Exercício 3
lista = []
texto = ''


arq = open('lista-cpf.txt', 'r',  encoding = 'utf-8')

for i, l in enumerate (arq):
     lista.append(l)
    


unique_list = [i for n, i in enumerate(lista) if i not in lista[n + 1:]]

for unique_result in unique_list:
    print(unique_result)




#len(unique_list)
#for unique_result in unique_list:
 #   print(unique_result)