# calculando a area de uma parede e quantos litros de tinta gastaria para pintar(cada litro de tinta pinta 2m^2)

print('Digite a seguir a altura e o comprimento da sua parede para saber quantos litros de tinta precisa')
print('***** Cada litro pinta o equivalente a 2 metros quadrados *****')

altura = float(input('Qual a altura da sua parede? '))
comprimento = float(input('Qual o comprimento? '))
area = altura * comprimento
litros = area / 2

print(f'A área da sua parede é {area}')
print(f'Sendo assim, gastaria {litros}l de tinta!')