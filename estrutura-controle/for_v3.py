produto = {'nome': 'Caneta Chic', 'preco': 14.99,
            'importada':True , 'estoque' : 793} 

for chaves in produto: 
    print(chaves) # percorre pela chave por padrao 
print('')

for valor in produto.values(): # percorre pelo valor
    print(valor) 
print('')

for chave, valor in produto.items(): # para percorrer chave e valor  
    print(f'{chave} = {valor}')