from random import randint


def sortear_dado():
    return randint(1, 6)


for numero_for in range(1, 7):
    if numero_for % 2 == 1:
        continue
    if numero_for == sortear_dado():
        print('ACERTOU', numero_for)
        break
else:
    print('Nao acertou o numero!')
