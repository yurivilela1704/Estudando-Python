#dolarize o valor dado
dolar = 5.49
nome = str(input('Qual seu nome ? '))
valor = float(input('Digite o valor em reais para saber o equivalente em dolar: '))
conversor = float(input(f'Olá {nome}, R$ {valor} em dolar equivale a U${valor / dolar:0.2f}'))
print(conversor)
