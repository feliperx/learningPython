# no python nao existe o switch como no C, Java..
# temos que fazer uma "gambiarrra" para ficar um estrutura semelhante
# usando dicionario


def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terca',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado'
    }
    # passamos um valor default caso o numero seja invalido
    return dias.get(dia, 'Invalido.')

if __name__ == '__main__': 
    for dia in range(0,9): 
        print(f'{dia} : {get_dia_semana(dia)}')
    
