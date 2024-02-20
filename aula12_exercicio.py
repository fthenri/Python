nome = "Lopes"
peso = 66
altura = 1.78
imc = peso / altura ** 2 

linha4 = f'IMC: {imc:.2f}' #formatei essa linha para poder diminuir a qntdd de casas decimais

print("Nome:", nome)
print("Peso:", peso)
print("Altura:", altura)
print(linha4)

# Verificação do IMC com base em tabelas

if imc < 17:
    print("Condição: Muito abaixo do peso")
elif imc < 18.5:
    print("Condição: Abaixo do peso ")
elif imc < 25:
    print("Condição: Peso Normal")
elif imc < 30:
    print("Condição: Acima do peso")
elif imc < 35:
    print("Condição: Obesidade grau I")
elif imc < 40.1:
    print("Condição: Obesidade grau II")
else:
    print("Condição: Obesidade grau III (mórbida)")