#while True: 
#    print('Vai demorar muitoooo!')

from random import randint

numero_informado = -1 
numero_secreto = randint(0,9) 


while numero_informado != numero_secreto: 
    numero_informado = (int(input('Informe um numero: '))) 

print(f'> Numero {numero_informado} eh o numero secreto! <')