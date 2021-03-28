import math


def circuferencia(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':  # se estiver no MÓDULO PRINCIPAL execute
    # identação, todos dentro da identação estão dentro do comando if
    raio = input("Informe o raio: ")
    area = circuferencia(raio)
    print('Area eh: ', area)
