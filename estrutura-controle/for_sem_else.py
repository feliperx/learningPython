# nao conseguimos criar constantes o python
# apenas convencoes com letras MAIUSCULAS, mas elas os valores podem se modificados

PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')  # "constantes"
textos = [
    'Felipe gosta de falar sobre futebol, religiao e politica',
    'A praia eh massa'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split(): 
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida: ', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado: ', texto)
