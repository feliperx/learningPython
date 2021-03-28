from math import pi
import sys


def circuferencia(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':  # se estiver no MÓDULO PRINCIPAL execute
    # identação, todos dentro da identação estão dentro do comando if
    # posso informar o raio junto com o arquivo.py no terminal
    print(sys.argv[1])
    raio = sys.argv[1]
    area = circuferencia(raio)
    print('Area eh: ', area)
