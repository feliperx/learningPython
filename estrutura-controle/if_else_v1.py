def nota_conceito(nota):

    if nota <= 10 and nota > 9:
        print('\nConceito: A\n')
    elif nota <= 9 and nota > 8:
        print('\nConceito: A-\n')
    elif nota <= 8 and nota > 7:
        print('\nConceito: B\n')
    elif nota <= 7 and nota > 6:
        print('\nConceito: B-\n')
    elif nota <= 6 and nota > 5:
        print('\nConceito: C\n')
    elif nota <= 5 and nota > 4:
        print('\nConceito: C-\n')
    elif nota <= 4 and nota > 3:
        print('\nConceito: D\n')
    elif nota <= 3 and nota > 2:
        print('\nConceito: D-\n')
    elif nota <= 2 and nota > 1:
        print('\nConceito: E\n')
    elif nota <= 1 and nota > 0:
        print('\nConceito: E-\n')
    else:
        print('\nINFORME UM NOTA VALIDA!\n')


if __name__ == '__main__':

    nota = input('\nInforme a nota: ')
    # nota eh lida como uma string, chamamos a funcao e convertemos para float
    nota_conceito(float(nota))
