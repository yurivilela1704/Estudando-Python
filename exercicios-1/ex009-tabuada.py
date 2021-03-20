# faça uma tabuada(ainda não a funcao pra fazer, mas deve ser enquanto)

valor = int(input('Digite um número: '))
print('#' * 12)
print(f'TABUADA DE {valor}')
print('#' * 12)

aux = 0
while (aux <= 10):
    print(f'{valor} X {aux:2} = {valor * aux}')
    aux = aux + 1

print('#' * 12)
