try:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    
    float_numero_1 = float(numero_1.replace(',', '.'))  # Substitui vírgulas por pontos, se houver
    float_numero_2 = float(numero_2.replace(',', '.'))

    soma = float_numero_1 + float_numero_2

    print(f'A soma dos números é: {soma}')

except ValueError:
    print('Por favor, insira números válidos.')
