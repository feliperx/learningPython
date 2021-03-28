import math


def circuferencia(raio):
    print('Area: {}'  .format(math.pi * float(raio) ** 2))


if __name__ == '__main__':  # se estiver no MÓDULO PRINCIPAL execute
    # identação, todos dentro da identação estão dentro do comando if
    raio = input("Informe o raio: ")
    circuferencia(raio)
