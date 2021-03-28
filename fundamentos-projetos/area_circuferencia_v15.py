from math import pi
import sys
import errno


class terminal_color:
    red = '\033[91m'  # cor vermelho
    white = '\033[0m'  # cor branca


def circuferencia(raio):
    return pi * float(raio) ** 2


def help():
    print('\nÉ necessário informar o raio da circuferencia!')
    # retorna o primeiro argumento, sem os 3 ultimos caracteres  '.py'
    print(f'Sintaxe: {sys.argv[0][:-3]} <raio>\n')


if __name__ == '__main__':  # se estiver no MÓDULO PRINCIPAL vai executar
    # IDENTAÇÃO, todos dentro da identação estão dentro do comando if
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)  # retorna 1, caso o problema der erro

    elif not sys.argv[1].isnumeric():  # se o argumento NÃO for numérico:
        help()
        print(
            f'\n{terminal_color.red}ERROR{terminal_color.white} - O valor informado não é numérico!\n')
        sys.exit(errno.EINVAL) # retorna o valor 22

    else:
        # posso informar o raio junto com o 'arquivo.py' no terminal
        print('\n>>> O raio é: ', sys.argv[1])
        raio = sys.argv[1]
        area = circuferencia(raio)
        print('\nA Área é: ', area)
        print('')
