


def saudacoes():
    print('a')

saudacoes()

#parametros

def saudacoes(nome, idade):
    print('Oi:',nome)
    print('Oi:',idade)
saudacoes('fabricio',25)


## defult parametros
def saudacoes(nome, idade=34):
    print('Oi:',nome)
    print('Oi:',idade)

saudacoes('fabricio')

#retorno

def soma(a,b):
    return a+b

print(soma(12,20))





