for number in range(1, 11):
    if number % 2 == 0:
        continue  # vai interromper a repeticao mas sem sair no laco, no caso, sempre que houver numeros pares vai voltar ao topo da funcao
    print(number) # imprimindo apenas o numeros impares de 1 - 11 

for x in range(1, 11):
    if x == 7: 
        print(x) 
        break # ele interrompe o laco
print('Fim')