numero1 = input("Digite um número: ")
numero2 = input("Digite outro número: ")

# Verifica se ambos os valores são compostos apenas por dígitos
if not numero1.isdigit() or not numero2.isdigit():
    print("Por favor, digite apenas números.")
else:
    numero1 = int(numero1)
    numero2 = int(numero2)

    if numero1 > numero2:
        print(f"O maior número é: {numero1}")
    elif numero1 == numero2:
        print(f"Os números são iguais: {numero1} = {numero2}")
    else:
        print(f"O maior número é: {numero2}")
