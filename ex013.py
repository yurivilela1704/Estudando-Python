# faça um reajuste no salário de um funcionário

nomeFuncionario = input('Digite o nome do funcionario: ')
salario = float(input('Digite o salário: R$'))
aumento = float(input('Porcentagem de aumento do salário(digitar valor em decimal ex.:0.5 = 50%):'))
reajuste = salario + (salario * aumento)

print(f'O salario do funcionario {nomeFuncionario} é R${salario}.')
print(f'{nomeFuncionario} recebeu aumento de {aumento *100}% e agora receberá R${reajuste}.')
