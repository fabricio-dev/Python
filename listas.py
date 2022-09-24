'''
fabricio esta testando listas

'''
notas=[9.5,8,10]

#criando listas
lista1=[]
lista2=list()
lista=['a',10,10.5,True]
lista=[10,[1,2,3]]


#indexaçao e fatiamento

lista2=['a',10,10.5,True]

print(lista[0])
print(lista[1])
#print(lista[2])
#print(lista[3])
#print(lista[-1])

#slaces pega um pedaço da lista um intervalo
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista[0:4])
print(lista[3:])
print(lista[0:8:2])

## percorrendo todos os elementos
for i in lista:
    print(i)


print('tamanho',len(lista))

for i in range(len(lista)):
    #print(i)

    print(lista[i])

#metodos de lista

#append
lista.append(22)## adiciona novo item no final da lista mas nao substitui nenhum

print(lista)


lista.insert(2,44)## adiciona novo item no indice escolhido
print(lista)

lista.extend(lista2)## adiciona a lista 2 no final da nista 1 junta as duas
print(lista)

lista.pop() #remove o ultimo por padrao perem se especificar o indice remove o elemento do indice indicado
print(lista)

lista.remove('a')#remove o elemento indicado ao primeiro q ele encontra

lista.index(10)# pega o idndice do elemento na lista

lista.sort(reverse=True)# ordena em ordem crescente por padrao revese faz o iverso

lista.count(10)#conta quantos elementos existe igua ao paramentro indicado



#funcoes para lista


print(len(lista))

print(sum(lista))

print(max(lista))

print(min(lista))


















