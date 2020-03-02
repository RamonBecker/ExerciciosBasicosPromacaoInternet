#!/usr/bin/python3

weekdays = ['mon','tues','wed','thurs','fri']


lista = ['a', 1, 3.14159265359]
#Como selecionar 'wed' pelo indice?

wed = int(input("Selecione wed:"))
print(weekdays[wed])


#Como verificar o tipo de 'mon'?

print(type(weekdays[0]))

#Como separar 'wed' até 'fri'?

days = weekdays[2::2] 

print("DAYS:",days)
# Quais as maneiras de selecionar 'fri' por indice?


fri = int(input("Selecione fri:"))

print(weekdays[fri])
i = 0

def indice(fri, i):
   if i == fri :
     return i
   else:
     i += 1
     return indice(fri, i)

print(weekdays[indice(fri, i)])


# Qual eh o tamanho dos dias e days_list?

print(len(weekdays[0]))
print(len(weekdays[1]))
print(len(weekdays[2]))
print(len(weekdays[3]))
print(len(weekdays[4]))

print(len(weekdays))



# Como inverter a ordem dos dias?

print(weekdays[::-1])

# Como inserir a palavra 'zero' entre 'a' e 1 de list?

lista.insert(1,"Zero")
print(lista)
#Como limpar list?
0

lista.clear()

#Como deletar list?

del lista

#Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?

ultimo_elemento = lista.pop(2)
