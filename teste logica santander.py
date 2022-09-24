

lista=[]



contador=30
cont2=0
for i in range(85,200000,7):
    print(i)
    
    print(i+contador)
   
    lista.append(i)
    lista.append(i+contador)
    
    
    contador=contador+1



print('-----------')
qtd=0

for i in range(len(lista)):

    if(lista[i]>1000 and lista[i]<1500 ):
        print(lista[i])
        qtd=qtd+1


    
print(qtd)

#if((i+contador>1000 and i+contador<1500) and (i+7 >1000 and i< 1500) ):