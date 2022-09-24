dicionario={}
diconario=dict()


dicionario={'nome':'fabricio','altura':1.85}


print(dicionario)


print(dicionario['altura'])

dicionario['idade']=25

print(dicionario)

dicionario['idade']=22
print(dicionario)


for i in dicionario:
    #print(i)
    print(i,dicionario[i])


print('peso' in dicionario)
print('nome' in dicionario)