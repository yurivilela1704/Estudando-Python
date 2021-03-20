# um programa que leia um valor em metros e converta-os para cm e mm(provavelmente deve existir funções para isso)

conversor = float(input('Digite o valor em metros que deseja converter: '))
mtocm = conversor * 100
mtomm = conversor * 1000
print(f'{conversor}m é igual a {mtocm}cm e {mtomm}mm')