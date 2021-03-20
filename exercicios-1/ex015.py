#calcular aluguel do carro em base em dias e KM rodados

kmRodado = float(input('Quantos km rodados? '))
diaAlugado = int(input('Quantos dias? '))
precoKM = kmRodado * 0.15
precoDia = diaAlugado * 60
precoTot = precoDia + precoKM

print(f'Como o carro teve {kmRodado}Km rodados nos seus {diaAlugado} dias alugados, o preço é R${precoTot:.2f}')
print(f'O valor cobrado pelos dias rodados foi de R${precoDia} e pela quilometragem R${precoKM}')
