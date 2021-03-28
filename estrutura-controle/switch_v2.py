# no python nao existe o switch como no C, Java..
# temos que fazer uma "gambiarrra" para ficar um estrutura semelhante
# usando dicionario simulamos um switch


def get_tipo_dia(dia):
    dias = {
        1: 'Fim de Semana',
        2: 'Dia de Samana',
        3: 'Dia de Samana',
        4: 'Dia de Samana',
        5: 'Dia de Samana',
        6: 'Dia de Samana',
        7: 'Fim de Semana'

    }
    # passamos um valor default caso o numero seja invalido
    return dias.get(dia, 'Invalido.')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia} : {get_tipo_dia(dia)}')
