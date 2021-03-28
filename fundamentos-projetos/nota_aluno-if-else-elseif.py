nota = input("\nInforme a nota: ") 
nota = float(nota)


def condicao_aluno(nota): 
    
    if nota >= 9: 
        print("\nAluno APROVADO e está no QUADRO DE HONRA!")
    elif nota >= 7: 
        print('\nAluno APROVADO!')
    elif nota >= 6: 
        print('\nAluno está de EXAME!') 
    else: 
        print('\nAluno está REPROVADO!') 

condicao_aluno(nota) 
print('')




    


