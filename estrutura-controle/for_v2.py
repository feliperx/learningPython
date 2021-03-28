palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=' - ')  # sem o end  o padrao de espaco = \n

print('\n')
for letra in palavra:
    print(letra)

procurados = ['Pedro', 'Maria', 'Taina', 'Felipe']  # lista

for nome in procurados:  # percorre a lista
    print(nome)

# percorre a lista e retorna o valor e o indice
for posicao, nome in enumerate(procurados):
    print(posicao, nome)

data_dia = ('Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta',
            'Sexta', 'Sabado')  # tupla

for dia in data_dia:
    print(f'Hoje eh {dia}')


# conjunto ou set, **set nao garante a ordem dos elementos
conjunto = set('1daeaed2234dadae')
conjunto2 = {1, 2, 3, 4, 5}

for letras in conjunto:
    print(letras)

for letras in conjunto2:
    print('\n', letras)
