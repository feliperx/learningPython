from math import pi
import sys


def circuferencia(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':  # se estiver no MÓDULO PRINCIPAL execute
    # identação, todos dentro da identação estão dentro do comando if
    if len(sys.argv) < 2:
        print('\nÉ necessário informar o raio da circuferencia!')
        print(f'Sintaxe: {sys.argv[0][:-3]} <raio>\n') # retorna o primeiro argumento, sem os 3 ultimos caracteres  '.py'

    else:
        # posso informar o raio junto com o arquivo.py no terminal
        print('\n>>> O raio é: ', sys.argv[1])
        raio = sys.argv[1]
        area = circuferencia(raio)
        print('\nA Área é: ', area)
        print('')
