# faça um programa que leia um preço e aplique desconto

print('*' * 20)
print('PROMOÇÃO')
print('*' * 20)

nomeProd = str(input('Digite o nome do produto: '))
preco = float(input('Digite um preço: '))
desconto = float(input('Digite o desconto em decimal(ex.: 50% = 0.5): '))
precodescontado = preco - (preco * desconto)

print(f'{nomeProd} é R${preco} e está com {desconto * 100}% de desconto, saindo por R${precodescontado:0.2f}')
