def idade_categoria(valor):

    idade = float(valor)

    if 0 < idade < 18:
        return 'Menor idade'

    elif idade in range(18, 59):  # range, intervalo entre valores
        return 'Adultos'

    elif idade in range(59, 100):  # o primeiro valor eh incluso no range, o ultimo nao
        return 'Melhor idade'

    elif idade >= 100:
        return 'Centenario'

    else:
        return 'Valor Invalido'


if __name__ == "__main__":
    for idade in (60, 18, 99, 100, 87, -2):
        print(f'{idade}: {idade_categoria(idade)}')
