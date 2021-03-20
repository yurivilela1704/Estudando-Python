# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ela

algo = input('Digite algo para descobrir qual o seu tipo? ')

print(type(algo))
print(f'Só tem espaços? {algo.isalnum()}')
print(f'faz parte do alfabeto? {algo.isalpha()}')
print(f'xxxxxxx? {algo.isascii()}')
print(f'Só tem espaços? {algo.isdigit()}')
print(f'Só tem espaços? {algo.isdecimal()}')
print(f'Só tem espaços? {algo.islower()}')
print(f'Só tem espaços? {algo.isupper()}')
print(f'Só tem espaços? {algo.isnumeric()}')
