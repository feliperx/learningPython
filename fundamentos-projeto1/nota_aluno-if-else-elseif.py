nota = input("\nInforme a nota: ")
nota = float(nota)


def condicao_aluno(nota):

    if nota >= 9:
        print("\nAluno APROVADO e esta no QUADRO DE HONRA!")
    elif nota >= 7:
        print('\nAluno APROVADO!')
    elif nota >= 6:
        print('\nAluno esta de EXAME!')
    else:
        print('\nAluno esta REPROVADO!')


condicao_aluno(nota)
print('')
