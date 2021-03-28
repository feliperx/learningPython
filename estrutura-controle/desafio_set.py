PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'}  # "constantes"
textos = [
    'Felipe gosta de falar sobre futebol , religiao e politica',
    'A praia eh massa'
] 

for texto in textos:
    # usando set (conjunto) e fazendo a intersecao entre o set e a lista
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split())) 
    if intersecao: # se estiver cheio retorna true
        print('Texto possui palavra(s) proibida(s): ', intersecao) 
    else: # vazio retorna false
        print('Texto autorizado: ', texto)    

# A vantagem eh que aparece todas as 'palavras proibidas' que estao na frase